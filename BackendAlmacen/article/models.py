from django.db import models
from company.models import Companies

class Articles(models.Model):
    id_mainarticle = models.CharField(primary_key=True)
    id_alternativearticle = models.CharField(max_length=20)
    name = models.CharField(max_length=50)
    stock = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    active = models.BooleanField(default=True)
    category = models.CharField(max_length=50)
    create_at = models.DateTimeField(auto_now_add=True)

class ArticleCompany(models.Model):
    article =  models.ForeignKey(Articles, on_delete=models.CASCADE)
    company = models.ForeignKey(Companies, on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = (('article', 'company'),)

    def __str__(self):
        return f"({self.article_id.name} , {self.company_id.name})"