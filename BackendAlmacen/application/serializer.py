from rest_framework import serializers
from .models import Request, Acceptance, RequestActions, Supply, ReturnExchange, Articles
from company.serializers import CompanySerializer
from company.models import Companies
from users.models import Users
from users.serializers import UserSerializer
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
    user = UserSerializer(read_only=True)
    collaborator = Collaboratorserializers(read_only=True)
    returnexchange = ReturnExchangeSerializer(read_only=True)

    class Meta:
        model = Supply
        fields = '__all__'

class RequestActionsSerializer(serializers.ModelSerializer):
    acceptance = serializers.PrimaryKeyRelatedField(
        queryset=Acceptance.objects.filter(request__status__in=['request', 'declined']),
        write_only=True
    )

    user=UserSerializer(read_only = True)
    supply = SupplySerializer(read_only=True)

    class Meta:
        model = RequestActions
        fields = [ 'id_RequestActions', 'user', 'acceptance', 'action', 'comment', 'requestactions_datetime', 'supply']
        read_only_fields = ['id_RequestActions', 'user', 'requestactions_datetime']

class AcceptanceSerializer(serializers.ModelSerializer):
    request_id = serializers.PrimaryKeyRelatedField(
        source='request', 
        queryset=Request.objects.filter(status='prerequest'),
        write_only=True
    )
    article = ArticleSerializers(read_only=True)
    user = UserSerializer(read_only=True)
    requestactions = RequestActionsSerializer(read_only=True)

    class Meta:
        model = Acceptance
        fields = ['id_acceptance', 'request_id', 'user', 'article', 'acceptance_datetime', 'requestactions']
        read_only_fields = ['id_acceptance', 'user', 'article', 'acceptance_datetime']

class RequestSerializer(serializers.ModelSerializer):
    supplierCompany = CompanySerializer(read_only=True)
    requestingCompany = CompanySerializer(read_only=True)
    user = UserSerializer( read_only= True)
    collaborator = Collaboratorserializers( read_only=True)
    acceptance = AcceptanceSerializer(read_only=True)
    article_obj = serializers.SerializerMethodField()
    article_price = serializers.SerializerMethodField()

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
        
    def get_article_obj(self, obj):
        try:
            if not obj.article:
                print(f"Request {obj.id_Request} no tiene artículo asignado")
                return None
            article_instance = Articles.objects.filter(id_mainarticle__iexact=obj.article).first()
            
            if not article_instance:
                print(f"❌ Artículo '{obj.article}' no encontrado para Request {obj.id_Request}")
                return None
    
            article_data = ArticleSerializers(article_instance).data
            print(f"✅ Request {obj.id_Request}: Artículo encontrado - {article_data.get('name')}")
            return article_data
        except Exception as e:
            print(f"Error obteniendo artículo para Request {obj.id_Request}: {str(e)}")
            return None

    def get_article_price(self, request):
        try:
            if not request.article:
                print(f"Request {request.id_Request} no tiene artículo asignado")
                return 0.00
            article = Articles.objects.filter(id_mainarticle__iexact=request.article).first()
            price = float(article.price) if article.price else 0.00
            print(f"Request {request.id_Request}: Artículo {article.id_mainarticle}, Precio: ${price}")
            return price
        except Articles.DoesNotExist:
            print(f"Artículo '{request.article}' no encontrado para Request {request.id_Request}")
            return 0.00
        except Exception as e:
            print(f"Error obteniendo precio para Request {request.id_Request}: {str(e)}")
            return 0.00