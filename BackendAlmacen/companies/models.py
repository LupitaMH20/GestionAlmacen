from django.db import models

class Companies(models.Model):
    id_Company = models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=200)

    def __str__(self):
        return super().__str__()
