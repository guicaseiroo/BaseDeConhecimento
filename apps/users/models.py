from django.db import models
from django.contrib.auth.models import AbstractUser

class Users(AbstractUser):
    CARGO_CHOICES = (
        ('1', 'Processos'),
        ('2', 'Usuário'),
    )
    cargo = models.CharField(
        max_length=1,
        choices=CARGO_CHOICES,
        null=True,
    )