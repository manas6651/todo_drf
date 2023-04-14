from rest_framework import serializers
from app.models import Todo



class TodoSerializer(serializers.ModelSerializer): 
    class Meta: 
        fields = '__all__'
        model = Todo