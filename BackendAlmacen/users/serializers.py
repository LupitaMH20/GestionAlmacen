from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import Users

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'
        
    def create(self, validated_data):
        password = validated_data.pop('password')
        validated_data['password'] = make_password(password)
        user = Users.objects.create(**validated_data)
        return user