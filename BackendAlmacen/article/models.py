from django.db import models

class Articles(models.Model):
    id_mainarticle = models.CharField(max_length=20, primary_key=True)
    id_alternativearticle = models.CharField(max_length=20)
    name = models.CharField(max_length=50)
    stock = models.IntegerField()
    money = models.DecimalField(max_digits=10, decimal_places=2)
    description =models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return super().__str__()
