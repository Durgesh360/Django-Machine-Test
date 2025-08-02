from rest_framework import serializers
from .models import Client, Project
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']

class ClientSerializer(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Client
        fields = '__all__'



class ProjectSerializer(serializers.ModelSerializer):
    users = UserSerializer(many=True, read_only=True)
    client = serializers.StringRelatedField(read_only=True)
    created_by = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Project
        fields = '__all__'
    


class SimpleProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'project_name']


class ClientDetailSerializer(serializers.ModelSerializer):
    projects = SimpleProjectSerializer(many=True, read_only=True)
    created_by = serializers.StringRelatedField()

    class Meta:
        model = Client
        fields = ['id', 'client_name', 'projects', 'created_at', 'created_by', 'updated_at']


class ProjectCreateSerializer(serializers.ModelSerializer):
    users = serializers.ListField(
        child=serializers.DictField(child=serializers.CharField()),
        write_only=True
    )

    class Meta:
        model = Project
        fields = ['project_name', 'users']

    def validate_users(self, value):
        user_ids = []
        for user in value:
            try:
                user_obj = User.objects.get(id=user['id'], username=user['username'])
                user_ids.append(user_obj.id)
            except User.DoesNotExist:
                raise serializers.ValidationError(f"User with id {user['id']} and username {user['username']} does not exist.")
        return user_ids

    def create(self, validated_data):
        user_ids = validated_data.pop('users')  # validated to be list of ids
        client_id = self.context['client_id']
        request = self.context['request']

        project = Project.objects.create(
            project_name=validated_data['project_name'],
            client_id=client_id,
            created_by=request.user
        )
        project.users.set(user_ids)
        return project

