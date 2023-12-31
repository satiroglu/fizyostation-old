# Generated by Django 4.2.3 on 2023-07-10 22:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('finance', '0002_alter_sales_options_alter_sales_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sales',
            name='status',
            field=models.IntegerField(choices=[(0, 'Aktif'), (1, 'Pasif')], default=1, verbose_name='Durum'),
        ),
        migrations.CreateModel(
            name='Branches',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='AVM adını yazınız', max_length=200, unique=True, verbose_name='Şube(AVM) Adı')),
                ('branchPhoto', models.CharField(max_length=200, unique=True, verbose_name='Şube Fotoğrafı')),
                ('manager', models.CharField(max_length=200, unique=True, verbose_name='Şube Müdürü')),
                ('phone', models.CharField(max_length=200, unique=True, verbose_name='Telefon')),
                ('email', models.CharField(max_length=200, unique=True, verbose_name='E-mail')),
                ('country', models.CharField(max_length=200, unique=True, verbose_name='Ülke')),
                ('city', models.CharField(max_length=200, unique=True, verbose_name='Şehir')),
                ('district', models.CharField(max_length=200, unique=True, verbose_name='İlçe')),
                ('postcode', models.CharField(max_length=200, verbose_name='Posta Kodu')),
                ('address', models.TextField(max_length=300, unique=True, verbose_name='Adres')),
                ('description', models.TextField(verbose_name='Adres Tarifi')),
                ('mon', models.CharField(default='12:00 - 15:00', max_length=200, unique=True, verbose_name='Pazartesi')),
                ('tue', models.CharField(default='12:00 - 15:00', max_length=200, unique=True, verbose_name='Salı')),
                ('wed', models.CharField(default='12:00 - 15:00', max_length=200, unique=True, verbose_name='Çarşamba')),
                ('thu', models.CharField(default='12:00 - 15:00', max_length=200, unique=True, verbose_name='Perşembe')),
                ('fri', models.CharField(default='12:00 - 15:00', max_length=200, unique=True, verbose_name='Cuma')),
                ('sat', models.CharField(default='12:00 - 15:00', max_length=200, unique=True, verbose_name='Cumartesi')),
                ('sun', models.CharField(default='12:00 - 15:00', max_length=200, unique=True, verbose_name='Pazar')),
                ('createdOn', models.DateTimeField(auto_now_add=True, verbose_name='Oluşturulma Tarihi')),
                ('updatedOn', models.DateTimeField(auto_now=True, verbose_name='Güncellenme Tarihi')),
                ('status', models.IntegerField(choices=[(0, 'Aktif'), (1, 'Pasif')], default=1, verbose_name='Durum')),
                ('author', models.ForeignKey(default='User', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Yazar')),
            ],
            options={
                'verbose_name': 'Şube',
                'verbose_name_plural': 'Şubeler',
                'ordering': ['-createdOn'],
            },
        ),
    ]
