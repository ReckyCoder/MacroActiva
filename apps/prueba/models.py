from django.db import models
# from model_utils.models import TimeStampedModel
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import UserManager

# Create your models here.

class User(AbstractBaseUser, PermissionsMixin):

    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(max_length=50)

    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'

    REQUIRED_FIELDS = ['email']

    objects = UserManager()
    
    class Meta:
        verbose_name = 'usuario'
        verbose_name_plural = 'usuarios'

    def __str__(self):
        return self.username

