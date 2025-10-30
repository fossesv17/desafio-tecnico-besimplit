## Desafio Tecnico - Besimplit - Full Stack Dev

#### Fabian Osses

Codigo para desafio tecnico como parte de postulación a Besimplit. Considera los requisitos minimos para el desafio tecnico y no incluye desarrollo de ningun bonus.

### Instrucciones

Corresponde a un proyecto Django y DRF, los requisitos son incluidos en un requirements.txt y pueden ser instalados con el comando.

    pip install -r requirements.txt

Desde el directorio base lo primero seria ejecutar migraciones para crear la base de datos con

    python .\app\manage.py makemigrations
    python .\app\manage.py migrate

A continuacion para poblar la base de datos con tareas de prueba se puede ejecutar el comando

    python .\app\manage.py populate_db .\app\task_list.json

Con la opcion de limpiar la base de datos agregando --wipe al comando

    python .\app\manage.py populate_db .\app\task_list.json --wipe

Con la base de datos poblada, se ejecuta el proyecto con el comando

    python .\app\manage.py runserver

La pagina queda corriendo en localhost:8000

### Explicacion solucion

Se presenta una vista simple con un listado de tareas, su nombre, descripcion, su estado de completitud, y acciones que se pueden hacer sobre las tareas. 


Acorde a los requisitos de la tarea, se puede crear nuevas tareas, actualizarla(nombre y descripcion), eliminar tareas y finalmente se puede modificar su estado de completitud de pendiente a completada.

Utilizando DRF se creo un viewset para tareas por lo que viene por defecto con una api en el endpoint, aqui deberia darnos una lista de tareas.

API y lista de tareas: [localhost:8000/api/tasks/](localhost:8000/api/tasks/)

Para crear tarea: [localhost:8000/api/tasks/](localhost:8000/api/tasks/create_task/)

Tarea especifica: [localhost:8000/api/tasks/\<id>/](localhost:8000/api/tasks/\<id>)

Para la implementacion se considero el tiempo y la poca experiencia con HTMX por lo que es una vista bastante simple y se priorizo cumplir los requisitos.

En caso de haber tenido mas tiempo, se mejoraria el aspecto visual, se agregarian filtros para ordenar tareas. 

Quiza considerar mas atributos como plazo para terminarla, quiza expandir la tabla para mostrar solo ciertas tareas.
