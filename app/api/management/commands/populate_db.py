import json
import os
from datetime import datetime
from django.core.management.base import BaseCommand, CommandError
from django.utils.dateparse import parse_datetime
from django.utils import timezone
from api.models import Task  # adjust to your model


task = [
    "Escribir", "Limpiar", "Ejercitar", "Ir a Farmacia", "Tejer", "Leer", "Tocar Piano", "Pintar un cuadro"
]

def parse_date(val):
    dt = parse_datetime(val)
    if dt is None:
        for fmt in ("%Y-%m-%d %H:%M", "%Y-%m-%d"):
            try:
                dt = datetime.strptime(val, fmt)
                dt = timezone.make_aware(dt)
                break
            except ValueError:
                continue
    else:
        if timezone.is_naive(dt):
            dt = timezone.make_aware(dt)
    return dt

class Command(BaseCommand):
    help = "Populate database"

    def add_arguments(self, parser):
        parser.add_argument(
            "json_path",
            type=str,
            help="Path to JSON file containing the tasks"
        )

        parser.add_argument(
            "--wipe",
            action="store_true",
            help="Delete existing tasks before importing JSON file"
        )

    def handle(self, *args, **options):
        json_path = options['json_path']
        wipe = options['wipe']

        if not os.path.exists(json_path):
            raise CommandError(f"File not found: {json_path}")
        
        self.stdout.write(self.style.NOTICE(f"Loading tasks from {json_path}..."))

        try:
            with open(json_path, "r", encoding="utf-8") as f:
                data = json.load(f)
        except json.JSONDecodeError as e:
            raise CommandError(f"Invalid JSON: {e}")

        if not isinstance(data, list):
            raise CommandError("JSON root must be a list of task objects.")

        if wipe:
            self.stdout.write(self.style.WARNING("Deleting existing tasks..."))
            Task.objects.all().delete()

        created_count = 0
        for entry in data:
            title = entry.get("title")
            if not title:
                self.stdout.write(self.style.WARNING("Skipping task with no title."))
                continue
            
            dt = entry.get("created_at")
            parsed_dt = parse_date(dt)

            task = Task.objects.create(
                title=title[:200],
                description=entry.get("description", ""),
                completed=entry.get("completed"),
                created_at=parsed_dt
            )

            created_count += 1

        self.stdout.write(self.style.SUCCESS(f"✅ Imported {created_count} tasks."))
    

