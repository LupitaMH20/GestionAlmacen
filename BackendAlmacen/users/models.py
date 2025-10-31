from django.db import models

class Users(models.Model):
    id_user = models.CharField(primary_key=True, max_length=20)
    name = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    admin = models.BooleanField(default=True)
    password = models.CharField(max_length=20)
    active = models.BooleanField(default=True)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return super().__str__()