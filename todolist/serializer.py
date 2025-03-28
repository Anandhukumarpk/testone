from rest_framework import serializers
from .models import todo


class TodoSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")

class TodoSereializer(serializers.ModelSerializer):
    class Meta:
        model = todo
        fields = ['id','title','description','completed','created_at']


