from django.db import models
from users.models import Users
from company.models import Companies
from article.models import Articles
from collaborator.models import Collaborators

# PreSolicitudes
class PreRequest(models.Model):
    id_PreRequest = models.AutoField(primary_key=True)
    supplierCompany = models.ForeignKey(Companies, on_delete=models.CASCADE, related_name='prerequests_as_supplier', null=True)
    requestingCompany = models.ForeignKey(Companies, on_delete=models.CASCADE, related_name='prerequests_as_requester', null=True)
    applicant = models.ForeignKey(Users, on_delete=models.CASCADE)
    collaborator = models.ForeignKey(Collaborators, on_delete=models.CASCADE, null=True, blank=True)
    type = models.CharField(max_length=20, null=True)
    article = models.CharField()
    description = models.TextField()
    amount = models.IntegerField()
    status = models.CharField(max_length=20, default='prerequest')
    order_workshop = models.TextField(null=True, blank=True)
    store = models.TextField(null=True, blank=True)
    requested_datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.id_prerRequest}- {self.status}"

# Solicitudes
class Request(models.Model):
    id_Request = models.AutoField(primary_key=True)
    prerequest = models.OneToOneField(PreRequest, on_delete=models.CASCADE, related_name='request')
    applicant = models.ForeignKey(Users, on_delete=models.CASCADE)
    article = models.ForeignKey(Articles, on_delete=models.CASCADE)
    collaborator = models.ForeignKey(Collaborators, on_delete=models.SET_NULL, null=True, blank=True, related_name='colaborations')
    supplierCompany = models.ForeignKey(Companies, on_delete=models.CASCADE, related_name='supplier')
    requestingCompany = models.ForeignKey(Companies, on_delete=models.CASCADE, related_name='requester')
    position = models.CharField(max_length=23)
    type = models.CharField(max_length=20)
    description = models.TextField()
    amount = models.IntegerField()
    status = models.CharField(max_length=20, default='request')
    order_workshop = models.TextField(null=True, blank=True)
    store = models.TextField(null=True, blank=True)
    request_datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.id_Request}-{self.status}"

# Autorizar
class Authorize(models.Model):
    id_Authorize = models.AutoField(primary_key=True)
    authorize = models.ForeignKey(Users, on_delete=models.CASCADE)
    request = models.OneToOneField(Request, on_delete=models.CASCADE, related_name='authorization')
    position = models.CharField(max_length=23)
    comment = models.TextField()
    status = models.CharField(max_length=20, default='authorized')
    authorized_datetime = models.DateTimeField(auto_now_add=True)
    
# Rechazar
class Decline(models.Model):
    id_Decline = models.AutoField(primary_key=True)
    decline = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='decline')
    request = models.OneToOneField(Request, on_delete=models.CASCADE, related_name='decline' )
    position = models.CharField(max_length=23)
    comment = models.TextField()
    status = models.CharField(max_length=20, default='declined')
    datetime = models.DateTimeField(auto_now_add=True)
    
# Surtir
class Deliverie(models.Model):
    id_Deliverie = models.AutoField(primary_key=True)
    request = models.OneToOneField(Request, on_delete=models.CASCADE, related_name='deliverie')
    persondelivery = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='delivery_made')
    personreceives = models.ForeignKey(Collaborators, on_delete=models.CASCADE, related_name='delivery_received')
    companydelivery = models.ForeignKey(Companies, on_delete=models.CASCADE, related_name='delivery_company')
    companyreceives = models.ForeignKey(Companies, on_delete=models.CASCADE, related_name='receiving_company')
    comment = models.TextField()
    photo = models.CharField(max_length=255, null=True)
    document = models.CharField(max_length=255, null=True)
    status = models.CharField(max_length=20, default='delivered')
    deliverie_datetime = models.DateTimeField(auto_now_add=True)

# Devolución o cambio
class ReturnExchange(models.Model):
    id_return_exchange = models.AutoField(primary_key=True)
    deliverie = models.OneToOneField(Deliverie, on_delete=models.CASCADE, related_name='return_exchange')
    returnenby = models.ForeignKey(Collaborators, on_delete=models.CASCADE, related_name='returned_by')
    receivedby = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='received_by')
    deliverycompany = models.ForeignKey(Companies, on_delete=models.CASCADE, related_name='delivery_company_return')
    receivingcompany = models.ForeignKey(Companies, on_delete=models.CASCADE, related_name='receiving_company_return')
    reason = models.TextField()
    type = models.CharField(max_length=10)
    return_datetime = models.DateTimeField(auto_now_add=True)