from rest_framework import serializers
from .models import PreRequest, Request, Authorize, Decline, Deliverie, ReturnExchange

class PreRequestSerializer(serializers.ModelSerializer):
    class Meta: 
        model = PreRequest
        fields = '__all__'

class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = '__all__'

class AuthorizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Authorize
        fields = '__all__'

class DeclineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Decline
        fields = '__all__'

class DeliverieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deliverie
        fields = '__all__'

class ReturnExchangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReturnExchange
        fields = '__all__'