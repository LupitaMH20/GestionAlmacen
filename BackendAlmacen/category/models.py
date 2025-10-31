from django.db import models
from article.models import Articles

class Category(models.Model):
    id_Category = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    active = models.BooleanField(default=True)
    create_at = models.DateTimeField(auto_now_add=True)

class CategoryArticle(models.Model):
    id_CatArticle = models.AutoField(primary_key=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    article = models.ForeignKey(Articles, on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = (('category', 'article'))

    def __str__(self):
        return f"({self.article_id.name} , {self.category_id.name})"