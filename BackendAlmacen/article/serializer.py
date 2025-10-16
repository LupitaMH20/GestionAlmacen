from rest_framework import serializers
from .models import Articles, ArticleCompany
from company.models import Companies

class ArticleSerializers(serializers.ModelSerializer):
    company_name = serializers.SerializerMethodField(read_only=True)
    company = serializers.CharField(write_only=True)
    class Meta:
        model = Articles
        fields = '__all__'
        
    def get_company_name(self, obj):
        try:
            relation = obj.articlecompany_set.first()
            if relation and relation.company:
                return relation.company.name
            return "Sin empresa"
        except AttributeError:
            return "N/A"

    def create(self, validated_data):
        company_id = validated_data.pop('company')
        article__instance = Articles.objects.create(**validated_data)

        try:
            company_instance = Companies.objects.get(id_Company=company_id)
            ArticleCompany.objects.create(
                article = article__instance,
                company = company_instance
            )
        except Companies.DoesNotExist:
            raise serializers.ValidationError({"company": "El ID de la empresa no existe"})
        
        return article__instance
    
    def update(self, instance, validated_data):
        if 'company' in validated_data:
            company_id = validated_data.pop('company')
            
            try:
                new_company_instance = Companies.objects.get(id_Company=company_id)
                relation, created = ArticleCompany.objects.get_or_create(
                    article=instance,
                    defaults={'company': new_company_instance}
                )
                if not created and relation.company != new_company_instance:
                    relation.company = new_company_instance
                    relation.save()
                elif created:
                    pass 

            except Companies.DoesNotExist:
                raise serializers.ValidationError({"company": "El ID de la empresa proporcionado no existe."})
            except Exception as e:
                raise serializers.ValidationError({"company": f"Error al actualizar la relación de empresa: {e}"})
        return super().update(instance, validated_data)