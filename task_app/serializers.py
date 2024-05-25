from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Client, Project

class ClientSerializer(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(source='created_by.username')
    projects = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Client
        fields = ['id', 'client_name', 'created_at', 'created_by', 'projects']

class ProjectSerializer(serializers.ModelSerializer):
    client = serializers.ReadOnlyField(source='client.client_name')
    users = serializers.SlugRelatedField(slug_field='username', queryset=User.objects.all(), many=True)
    created_by = serializers.ReadOnlyField(source='created_by.username')

    class Meta:
        model = Project
        fields = ['id', 'project_name', 'client', 'users', 'created_at', 'created_by', 'updated_at']
