from rest_framework import serializers
from .models import Collaborators, CollaboratorCompany
from company.models import Companies

class Collaboratorserializers(serializers.ModelSerializer):
    company_name = serializers.SerializerMethodField(read_only=True)
    company =serializers.CharField(write_only=True)
    class Meta:
        model = Collaborators
        fields = '__all__'
    
    def get_company_name(self, obj):
        try:
            relation = obj.collaboratorcompany_set.first()
            if relation and relation.company:
                return relation.company.name
            return "Sin empresa"
        except AttributeError:
            return "N/A"

    def create(self, validated_data):
        company_id = validated_data.pop('company')
        collaborator__instance = Collaborators.objects.create(**validated_data)

        try:
            company_instance = Companies.objects.get(id_Company=company_id)
            CollaboratorCompany.objects.create(
                collaborator = collaborator__instance,
                company = company_instance
            )
        except Companies.DoesNotExist:
            raise serializers.ValidationError({"company": "El ID de la empresa no existe"})
        
        return collaborator__instance
    
    def update(self, instance, validated_data):
        if 'company' in validated_data:
            company_id = validated_data.pop('company')
            
            try:
                new_company_instance = Companies.objects.get(id_Company=company_id)
                relation, created = CollaboratorCompany.objects.get_or_create(
                    collaborator=instance,
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