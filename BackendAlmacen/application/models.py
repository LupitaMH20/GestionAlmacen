from django.db import models
from users.models import Users
from company.models import Companies
from article.models import Articles
from collaborator.models import Collaborators

class Request(models.Model):
    id_Request = models.AutoField(primary_key=True)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    article = models.ForeignKey(Articles, on_delete=models.CASCADE)
    collaborator = models.ForeignKey(Collaborators, on_delete=models.SET_NULL, null=True, blank=True, related_name='colaborations')
    supplierCompany = models.ForeignKey(Companies, on_delete=models.CASCADE, related_name='supplier')
    requestingCompany = models.ForeignKey(Companies, on_delete=models.CASCADE, related_name='requester')
    type = models.CharField(max_length=20)
    description = models.TextField()
    amount = models.IntegerField()
    status = models.CharField(max_length=20, default='request')
    order_workshop = models.TextField(null=True, blank=True)
    store = models.TextField(null=True, blank=True)
    request_datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.id_Request}-{self.status}"

class Acceptance(models.Model):
    id_acceptance = models.AutoField(primary_key=True)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    request = models.ForeignKey(Request, on_delete=models.CASCADE)
    acceptance_datetime = models.DateTimeField(auto_now_add=True)

class RequestActions(models.Model):
    id_RequestActions = models.AutoField(primary_key=True)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    request = models.OneToOneField(Request, on_delete=models.CASCADE)
    comment = models.TextField()
    requestactions_datetime = models.DateTimeField(auto_now_add=True)

class Supply(models.Model):
    id_supply = models.AutoField(primary_key=True)
    requestActions = models.OneToOneField(RequestActions, on_delete=models.CASCADE)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    collabortor = models.ForeignKey(Collaborators, on_delete=models.CASCADE)
    comment = models.TextField()
    photo = models.CharField(max_length=255, null=True)
    document = models.CharField(max_length=255, null=True)
    supply_datetime = models.DateTimeField(auto_now_add=True)

class ReturnExchange(models.Model):
    id_returnExchange = models.AutoField(primary_key=True)
    supply = models.OneToOneField(Supply, on_delete=models.CASCADE)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    collaborator = models.ForeignKey(Collaborators, on_delete=models.CASCADE)
    reason = models.TextField()
    return_datetime = models.DateTimeField(auto_now_add=True)