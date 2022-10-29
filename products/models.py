from django.db import models
from accounts.models import AbstractUser


class Product(models.Model):

    CATEGORY_CHOICES = [
        ('milk', 'Молочные'),
        ('meat', 'Мясные'),
        ('bread', 'Хлебобулочные'),
        ('juice', 'Соки'),
        ('other', 'Разное'),
    ]

    name = models.CharField(verbose_name='Наименование', max_length=100, null=False)
    description = models.TextField(verbose_name='Описание', max_length=2000, null=True, blank=True)
    category = models.CharField(
        verbose_name='Категория', 
        max_length=10, 
        choices=CATEGORY_CHOICES, 
        default='other'
        )
    image = models.CharField(verbose_name='Категория', default='image', null=True)


    def __str__(self):
        return self.name
