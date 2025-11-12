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
    
    # 1. Nombramos el campo 'request_id' (para coincidir con Vue y Meta)
    request_id = serializers.PrimaryKeyRelatedField(
        # 2. Ahora 'source' SÍ es necesario, porque 'request_id'
        #    apunta al campo 'request' del modelo.
        source='request', 
        queryset=Request.objects.filter(status='prerequest'),
        write_only=True
    )
    
    # (Tus otros campos están bien)
    article = ArticleSerializers(read_only=True)
    user = UserSerializer(read_only=True)

    class Meta:
        model = Acceptance
        # 3. La lista 'fields' ahora SÍ coincide con el campo 'request_id'
        fields = ['id_acceptance', 'request_id', 'user', 'article', 'acceptance_datetime']
        read_only_fields = ['id_acceptance', 'user', 'article', 'acceptance_datetime']

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