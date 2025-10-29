from django.urls import path, include
from .views import home
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet

router = DefaultRouter()
router.register(r'tasks', TaskViewSet)

urlpatterns = [
    path('', home, name='home'),
    path('api/', include(router.urls))
]