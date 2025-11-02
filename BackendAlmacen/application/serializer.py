from rest_framework import serializers
from .models import Request, Acceptance, RequestActions, Supply, ReturnExchange
from company.serializers import CompanySerializer
from company.models import Companies
from users.models import Users
from users.serializers import UserSerializer
from article.models import Articles
from article.serializer import ArticleSerializers
from collaborator.models import Collaborators
from collaborator.serializer import Collaboratorserializers

class ReturnExchangeSerializer(serializers.ModelSerializer):
    supply = serializers.PrimaryKeyRelatedField(queryset=Supply.objects.all())
    user = serializers.PrimaryKeyRelatedField(queryset=Users.objects.all())
    collaborator = serializers.PrimaryKeyRelatedField(queryset=Collaborators.objects.all())

    class Meta:
        model = ReturnExchange
        fields = '__all__'

class SupplySerializer(serializers.ModelSerializer):
    requestActions = serializers.PrimaryKeyRelatedField(queryset=RequestActions.objects.all())
    user = serializers.PrimaryKeyRelatedField(queryset=Users.objects.all())
    collaborator = serializers.PrimaryKeyRelatedField(queryset=Collaborators.objects.all())
    returnexchange = ReturnExchangeSerializer(read_only=True)

    class Meta:
        model = Supply
        fields = '__all__'

class RequestActionsSerializer(serializers.ModelSerializer):
    acceptance = serializers.PrimaryKeyRelatedField(queryset=Acceptance.objects.all())
    user = serializers.PrimaryKeyRelatedField(queryset=Users.objects.all())
    supply = SupplySerializer(read_only=True)

    class Meta:
        model = RequestActions
        fields = '__all__'

class AcceptanceSerializer(serializers.ModelSerializer):
    request = serializers.PrimaryKeyRelatedField(queryset=Request.objects.all())
    article = serializers.PrimaryKeyRelatedField(queryset=Articles.objects.all())
    user = serializers.PrimaryKeyRelatedField(queryset=Users.objects.all())
    requestactions = RequestActionsSerializer(read_only=True)

    class Meta:
        model = Acceptance
        fields = '__all__'

class RequestSerializer(serializers.ModelSerializer):
    supplierCompany = CompanySerializer(read_only=True)
    requestingCompany = CompanySerializer(read_only=True)
    user = UserSerializer( read_only= True)
    collaborator = Collaboratorserializers( read_only=True)
    acceptance = AcceptanceSerializer(read_only=True)

    supplierCompany_id = serializers.PrimaryKeyRelatedField(
        queryset=Companies.objects.all(),
        source = 'supplierCompany',
        write_only = True)
    
    requestingCompany_id = serializers.PrimaryKeyRelatedField(
        queryset=Companies.objects.all(),
        source = 'requestingCompany',
        write_only = True)
    
    user_id = serializers.PrimaryKeyRelatedField(
        queryset=Users.objects.all(),
        source='user',
        write_only=True
    )

    collaborator_id = serializers.PrimaryKeyRelatedField(
        queryset=Collaborators.objects.all(),
        source='collaborator',
        write_only=True,
        allow_null=True
    )
    
    class Meta: 
        model = Request
        fields = '__all__'