from django.db import models

class Collaborators(models.Model):
    id_Collaborator = models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    active = models.BooleanField(default=True)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return super().__str__()