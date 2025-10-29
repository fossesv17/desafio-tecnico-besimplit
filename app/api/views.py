from rest_framework import viewsets
from rest_framework.decorators import action
from .models import Task
from .serializers import TaskSerializer 
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .forms import TaskForm

# Create your views here.


def home(request):
    return render(request, 'tasks.html')

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    @action(detail=False, methods=['get'])
    def task_list(self, request):
        tasks = self.get_queryset()        
        return render(request, 'fragments/task_list_fragment.html', { 'tasks' : tasks })
    
    @action(detail=False, methods=['get', 'post'])
    def create_task(self, request):
        if request.method == 'POST':
            form = TaskForm(request.POST)
            if form.is_valid():
                form.save()
                
                response = HttpResponse()
                response['HX-Trigger'] = 'taskListUpdate'
                response.write("<script>document.getElementById('modal-container').innerHTML = '';</script>")

                return response
            
        else:
            form = TaskForm()
            
        return render(request, 'fragments/create_task_form.html', { 'form' : form })     
    
    @action(detail=True, methods=['get', 'post'])
    def edit_task(self, request, pk=None):
        if pk:
            task = get_object_or_404(Task, pk=pk)
        else:
            task = None

        if request.method == 'POST':
            form = TaskForm(request.POST, instance=task)
            if form.is_valid():
                form.save()
                
                response = HttpResponse()
                response['HX-Trigger'] = 'taskListUpdate'
                response.write("<script>document.getElementById('modal-container').innerHTML = '';</script>")
                return response
        else:
            form = TaskForm(instance=task)
            
        return render(request, 'fragments/edit_task_form.html', { 'form' : form }) 
    
    @action(detail=True, methods=['delete', 'get', 'post'])
    def delete_task(self, request, pk=None):
        task = get_object_or_404(Task, pk=pk)

        if request.method in ['DELETE', 'POST']:
            print(request.method)
            task.delete()
            response = HttpResponse()
            response['HX-Trigger'] = 'taskListUpdate'
            response.write("<script>document.getElementById('modal-container').innerHTML = '';</script>")
            return response
    
        else:
            return render(request, 'fragments/delete_task_confirmation.html', { 'task' : task })
        
    @action(detail=True, methods=['post'])
    def change_task_status(self, request, pk=None):
        task = get_object_or_404(Task, pk=pk)
        print(task)

        task.completed = not task.completed

        task.save()
        response = HttpResponse()
        response['HX-Trigger'] = 'taskListUpdate'
        return response