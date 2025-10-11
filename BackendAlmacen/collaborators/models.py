from django.db import models

class Collaborators(models.Model):
    id_Collaborator = models.CharField(max_length=20)
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    position = models.CharField(max_length=50)

    def __str__(self):
        return super().__str__()