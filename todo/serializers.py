from rest_framework import serializers
from .models import ToDo
from django.contrib.auth import get_user_model

User = get_user_model()


class ToDoSerializer(serializers.ModelSerializer):

    def validate_priority(self, priority):
        if priority > 10 or priority < 0 :
            raise serializers.ValidationError('Invalid...')
        return priority

    class Meta:
        model = ToDo
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    todos = ToDoSerializer(read_only=True, many=True)
    class Meta:
        model = User
        fields = '__all__'       