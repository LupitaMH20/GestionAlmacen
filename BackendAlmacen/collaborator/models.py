from django.db import models
from company.models import Companies

class Collaborators(models.Model):
    id_Collaborator = models.CharField(primary_key=True)
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    active = models.BooleanField(default=True)
    create_at = models.DateTimeField(auto_now_add=True)

class CollaboratorCompany(models.Model):
    company = models.ForeignKey(Companies, on_delete=models.CASCADE)
    collaborator = models.ForeignKey(Collaborators, on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = (('collaborator', 'company'),)


    def __str__(self):
        return f"{self.collaborator_id.name} - {self.company_id.name}"