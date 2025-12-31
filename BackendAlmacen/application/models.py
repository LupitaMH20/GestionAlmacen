from django.db import models
from users.models import Users
from company.models import Companies
from article.models import Articles
from collaborator.models import Collaborators

class Request(models.Model):
    id_Request = models.AutoField(primary_key=True)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    collaborator = models.ForeignKey(Collaborators, on_delete=models.SET_NULL, null=True, blank=True, related_name='colaborations')
    supplierCompany = models.ForeignKey(Companies, on_delete=models.CASCADE, related_name='supplier')
    requestingCompany = models.ForeignKey(Companies, on_delete=models.CASCADE, related_name='requester')
    article = models.CharField(max_length=100)
    type = models.CharField(max_length=20)
    description = models.TextField()
    amount = models.IntegerField()
    status = models.CharField(max_length=20, default='prerequest')
    order_workshop = models.TextField(null=True, blank=True)
    store = models.TextField(null=True, blank=True)
    is_paid = models.BooleanField(default=False)
    request_datetime = models.DateTimeField(auto_now_add=True)
    archived_datetime = models.DateTimeField(null=True, blank=True)
    rejection_reason = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.id_Request}-{self.status}"

class Acceptance(models.Model):
    id_acceptance = models.AutoField(primary_key=True)
    article = models.ForeignKey(Articles, on_delete=models.CASCADE)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    request = models.OneToOneField(Request, on_delete=models.CASCADE)
    acceptance_datetime = models.DateTimeField(auto_now_add=True)

class RequestActions(models.Model):
    id_RequestActions = models.AutoField(primary_key=True)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    acceptance = models.OneToOneField(Acceptance, on_delete=models.CASCADE)
    ACTION_CHOICES = [
        ('authorized', 'Autorizado'),
        ('declined', 'Rechazado'),
    ]
    action = models.CharField(max_length=10, choices=ACTION_CHOICES)
    comment = models.TextField()
    requestactions_datetime = models.DateTimeField(auto_now_add=True)

class Supply(models.Model):
    id_supply = models.AutoField(primary_key=True)
    requestActions = models.OneToOneField(RequestActions, on_delete=models.CASCADE)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    collaborator = models.ForeignKey(Collaborators, on_delete=models.CASCADE)
    comment = models.TextField()
    document = models.FileField(upload_to='supplies/', null=True, blank=True)
    supply_datetime = models.DateTimeField(auto_now_add=True)
    
    PAYMENT_STATUS_CHOICES = [
        ('paid', 'Pagado'),
        ('unpaid', 'No Pagado'),
    ]
    payment_status = models.CharField(
        max_length=10, 
        choices=PAYMENT_STATUS_CHOICES, 
        default='unpaid',
        help_text='Estado de pago para solicitudes de Consumo Personal'
    )

    # ✅ NUEVOS CAMPOS PARA SUPABASE
    document_url = models.URLField(max_length=500, blank=True, null=True)  # URL pública del PDF
    document_path = models.CharField(max_length=300, blank=True, null=True)  # Ruta en Supabase

    def __str__(self):
        return f"Supply-{self.id_supply}"
    
class ReturnExchange(models.Model):
    id_returnExchange = models.AutoField(primary_key=True)
    supply = models.OneToOneField(Supply, on_delete=models.SET_NULL, null=True, blank=True)
    user = models.ForeignKey(Users, on_delete=models.SET_NULL, null=True, blank=True)
    collaborator = models.ForeignKey(Collaborators, on_delete=models.SET_NULL, null=True, blank=True)
    reason = models.TextField()
    returnE_datetime = models.DateTimeField(auto_now_add=True)