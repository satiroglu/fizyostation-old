# Generated by Django 4.2.3 on 2023-07-10 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0004_alter_branches_city_alter_branches_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sales',
            name='status',
            field=models.IntegerField(choices=[(0, 'Aktif'), (1, 'Pasif')], default=0, verbose_name='Durum'),
        ),
    ]