from rest_framework import serializers
from .models import PreRequest, Request, Authorize, Decline, Deliverie, ReturnExchange
from company.serializers import CompanySerializer
from company.models import Companies
from users.models import Users
from users.serializers import UserSerializer
from collaborator.models import Collaborators
from collaborator.serializer import Collaboratorserializers

class PreRequestSerializer(serializers.ModelSerializer):
    supplierCompany = CompanySerializer(read_only=True)
    requestingCompany = CompanySerializer(read_only=True)
    applicant = UserSerializer( read_only= True)
    collaborator = Collaboratorserializers( read_only=True)

    supplierCompany_id = serializers.PrimaryKeyRelatedField(
        queryset=Companies.objects.all(),
        source = 'supplierCompany',
        write_only = True)
    
    requestingCompany_id = serializers.PrimaryKeyRelatedField(
        queryset=Companies.objects.all(),
        source = 'requestingCompany',
        write_only = True)
    
    applicant_id = serializers.PrimaryKeyRelatedField(
        queryset=Users.objects.all(),
        source='applicant',
        write_only=True
    )

    collaborator_id = serializers.PrimaryKeyRelatedField(
        queryset=Collaborators.objects.all(),
        source='collaborator',
        write_only=True,
        allow_null=True
    )
    
    class Meta: 
        model = PreRequest
        fields = '__all__'

class RequestSerializer(serializers.ModelSerializer):
    prerequest = serializers.PrimaryKeyRelatedField(queryset=PreRequest.objects.all())
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