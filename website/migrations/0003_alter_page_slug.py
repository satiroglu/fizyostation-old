# Generated by Django 4.2.3 on 2023-07-10 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_remove_branch_logo_alter_branch_author_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='slug',
            field=models.SlugField(max_length=200, unique=True, verbose_name='Slug'),
        ),
    ]
