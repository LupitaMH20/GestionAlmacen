from rest_framework import serializers
from .models import Collaborators

class Collaboratorserializers(serializers.ModelSerializer):
    class Meta:
        model = Collaborators
        fields = '__all__'