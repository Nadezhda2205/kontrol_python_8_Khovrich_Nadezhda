from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator

class Product(models.Model):

    CATEGORY_CHOICES = [
        ('milk', 'Молочные'),
        ('meat', 'Мясные'),
        ('bread', 'Хлебобулочные'),
        ('juice', 'Соки'),
        ('other', 'Разное'),
    ]

    name = models.CharField(verbose_name='Наименование', max_length=100, null=False)
    description = models.TextField(verbose_name='Описание', max_length=2000, null=False)
    category = models.CharField(
        verbose_name='Категория', 
        max_length=10, 
        choices=CATEGORY_CHOICES, 
        default='other',
        null=False,
        )
    image = models.TextField(verbose_name='Изображение', default='image', null=True)


    def __str__(self):
        return self.name

class Comment(models.Model):

    CATEGORY_CHOICES = [
        ('one', '1'),
        ('two', '2'),
        ('three', '3'),
        ('four', '4'),
        ('five', '5'),
    ]
    author = models.ForeignKey(verbose_name='Автор', to=get_user_model(), related_name='comments', null=False,
                               blank=False,
                               on_delete=models.CASCADE)
    product = models.ForeignKey(verbose_name='Продукт', to=Product, related_name='comments', null=False,
                             blank=False, on_delete=models.CASCADE)
    text = models.CharField(verbose_name='Текст', null=False, blank=False, max_length=500)
    created_at = models.DateTimeField(auto_now_add = True)
    valuation = models.IntegerField(default=1, validators=[MaxValueValidator(5), MinValueValidator(1)])

