# Generated by Django 4.2.3 on 2023-07-14 00:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0019_alter_sales_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='sales',
            name='branch',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='finance.branches'),
        ),
    ]
