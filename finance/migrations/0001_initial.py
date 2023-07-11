# Generated by Django 4.2.3 on 2023-07-10 21:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Sales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=200, unique=True, verbose_name='Kartlı Satış')),
                ('credit', models.CharField(max_length=200, unique=True, verbose_name='Kartlı Satış')),
                ('cash', models.CharField(max_length=200, unique=True, verbose_name='Nakit Satış')),
                ('expense', models.SlugField(max_length=200, unique=True, verbose_name='Gider')),
                ('remain', models.CharField(default='headerPhoto', max_length=200, unique=True, verbose_name='Kalan')),
                ('turnover', models.TextField(verbose_name='Ciro')),
                ('createdOn', models.DateTimeField(auto_now_add=True, verbose_name='Oluşturulma Tarihi')),
                ('updatedOn', models.DateTimeField(auto_now=True, verbose_name='Güncellenme Tarihi')),
                ('status', models.IntegerField(choices=[(0, 'Taslak'), (1, 'Yayınla')], default=1, verbose_name='Durum')),
                ('author', models.ForeignKey(default='User', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Kaydeden')),
            ],
            options={
                'verbose_name': ' Satışlar',
                'verbose_name_plural': ' Satışlar',
                'ordering': ['-createdOn'],
            },
        ),
    ]
