from rest_framework import routers
from .views import TareaViewSet
from django.urls import path, include
router = routers.DefaultRouter()
router.register(r'tareas', TareaViewSet)
urlpatterns = [
    path('', include(router.urls)),
]
from django.contrib import admin
from django.urls import path
from tarea.views import TareaViewSet

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TareaViewSet, name='inicio'),
]
