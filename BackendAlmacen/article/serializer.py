from rest_framework import serializers
from .models import Articles, ArticleCompany
from company.models import Companies
from category.models import Category, CategoryArticle

class ArticleSerializers(serializers.ModelSerializer):
    company_name = serializers.SerializerMethodField(read_only=True)
    company = serializers.CharField(write_only=True)
    category_name = serializers.SerializerMethodField(read_only=True)
    category = serializers.CharField(write_only=True)

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
        
    
    def get_category_name(self, obj):
        try:
            relation = obj.categoryarticle_set.first()
            if relation and relation.category:
                return relation.category.name
            return "Sin categoria"
        except AttributeError:
            return "N/A"

    def create(self, validated_data):
        company_id = validated_data.pop('company')
        category_id = validated_data.pop('category')

        # Crear el artículo
        article_instance = Articles.objects.create(**validated_data)

        # Relación con Company
        try:
            company_instance = Companies.objects.get(id_Company=company_id)
            ArticleCompany.objects.create(
                article=article_instance,
                company=company_instance
            )
        except Companies.DoesNotExist:
            raise serializers.ValidationError({"company": "El ID de la empresa no existe"})

        # Relación con Category
        try:
            category_instance = Category.objects.get(id_Category=category_id)
            CategoryArticle.objects.create(
                article=article_instance,
                category=category_instance
            )
        except Category.DoesNotExist:
            raise serializers.ValidationError({"category": "El ID de la categoría no existe"})

        return article_instance
    
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
    
        if 'category' in validated_data:
            category_id = validated_data.pop('category')

            try:
                new_category_instance = Category.objects.get(id_Category=category_id)
                relation, created = Articles.objects.get_or_create(
                    article = instance,
                    defaults = {'category': new_category_instance}
                )
                if not created and relation.category != new_category_instance:
                    relation.category = new_category_instance
                    relation.save()
                elif created:
                    pass
            except Category.DoesNotExist:
                raise serializers.ValidationError({"category": "El ID de la categoria no existe"})
            except Exception as e:
                raise serializers.ValidationError({"category": f"error al actualizar la relacion: {e}"})
        return super().update(instance,validated_data)