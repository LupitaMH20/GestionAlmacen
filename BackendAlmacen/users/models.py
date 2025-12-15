# En users/models.py
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class UsersManager(BaseUserManager):
    
    def create_user(self, name, id_user, password=None, **extra_fields):
        if not name:
            raise ValueError('El campo "name" es obligatorio')
        if not id_user:
            raise ValueError('El campo "id_user" es obligatorio')
        
        user = self.model(
            name=name,
            id_user=id_user,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, name, id_user, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('admin', True)
        extra_fields.setdefault('active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('El superusuario debe tener is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('El superusuario debe tener is_superuser=True.')
        
        return self.create_user(name, id_user, password, **extra_fields)

class Users(AbstractBaseUser, PermissionsMixin):
    id_user = models.CharField(primary_key=True, max_length=20) 
    name = models.CharField(max_length=50, unique=True)
    position = models.CharField(max_length=50, blank=True, null=True)
    admin = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    create_at = models.DateTimeField(auto_now_add=True)

    is_staff = models.BooleanField(default=False) 
    objects = UsersManager()
    USERNAME_FIELD = 'name'
    REQUIRED_FIELDS = ['id_user'] 
    @property
    def is_active(self):
        "¿Está el usuario activo?"
        return self.active

    def __str__(self):
        return self.name