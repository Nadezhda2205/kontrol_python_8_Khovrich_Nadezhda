# Generated by Django 4.1.1 on 2022-10-29 06:13

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Наименование')),
                ('description', models.TextField(max_length=2000, verbose_name='Описание')),
                ('category', models.CharField(choices=[('milk', 'Молочные'), ('meat', 'Мясные'), ('bread', 'Хлебобулочные'), ('juice', 'Соки'), ('other', 'Разное')], default='other', max_length=10, verbose_name='Категория')),
                ('image', models.TextField(default='image', null=True, verbose_name='Изображение')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=500, verbose_name='Текст')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('valuation', models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)])),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='products.product', verbose_name='Продукт')),
            ],
        ),
    ]