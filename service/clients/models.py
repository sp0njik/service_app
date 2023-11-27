from django.db import models
from django.contrib.auth.models import User


class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    company_name = models.CharField(max_length=100, verbose_name='название компании')
    full_address = models.CharField(max_length=100, verbose_name='адрес')

    def __str__(self):
        return f'Client:{self.company_name}'
