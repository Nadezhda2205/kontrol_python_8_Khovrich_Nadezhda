from django.db import models

from random import choices
from django.contrib.auth.models import AbstractUser
from django.db import models




class Account(AbstractUser):

    
    about = models.TextField(
        null=True,
        blank=True,
        verbose_name='Информация'
    )
    phone = models.CharField(
        null=True,
        blank=True,
        verbose_name='Телефон',
        max_length=15

    )

    
    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'


