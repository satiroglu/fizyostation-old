# Generated by Django 4.2.3 on 2023-07-13 22:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cities_light', '0011_alter_city_country_alter_city_region_and_more'),
        ('finance', '0012_rename_description_branches_addressdescription_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='branches',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cities_light.city', verbose_name='Ülke'),
        ),
    ]
