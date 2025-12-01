from models import Tarea
from rest_framework import serializers
class TareaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarea
        fields = ['id', 'titulo', 'descripcion', 'fecha_creacion', 'fecha_vencimiento', 'completada']