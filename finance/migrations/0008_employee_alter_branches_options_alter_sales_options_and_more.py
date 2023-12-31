# Generated by Django 4.2.3 on 2023-07-14 17:39

import cities_light.models
from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cities_light', '0011_alter_city_country_alter_city_region_and_more'),
        ('finance', '0007_alter_sales_options_alter_sales_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.IntegerField(choices=[(0, 'Kadın'), (1, 'Erkek')], verbose_name='Cinsiyet')),
                ('firstName', models.CharField(max_length=150, verbose_name='Adı')),
                ('lastName', models.CharField(max_length=150, verbose_name='Soyadı')),
                ('dateOfBirth', models.DateField(blank=True, verbose_name='Doğum Tarihi')),
                ('dateOfJoin', models.DateField(blank=True, verbose_name='İşe Giriş Tarihi')),
                ('dateOfQuit', models.DateField(blank=True, verbose_name='İşten Çıkış Tarihi')),
            ],
            options={
                'verbose_name': 'Personeller',
                'verbose_name_plural': 'Personeller',
                'ordering': ['-firstName'],
            },
        ),
        migrations.AlterModelOptions(
            name='branches',
            options={'ordering': ['-createdOn'], 'verbose_name': 'Şubeler', 'verbose_name_plural': 'Şubeler'},
        ),
        migrations.AlterModelOptions(
            name='sales',
            options={'ordering': ['-createdOn'], 'verbose_name': 'Satışlar', 'verbose_name_plural': 'Satışlar'},
        ),
        migrations.RemoveField(
            model_name='branches',
            name='branchPhoto',
        ),
        migrations.RemoveField(
            model_name='branches',
            name='description',
        ),
        migrations.AddField(
            model_name='branches',
            name='addressDescription',
            field=models.CharField(blank=True, help_text='Maksimum 300 karakter. Şubeye nasıl ulaşılabileceği hakkında bilgi yazın.', max_length=300, verbose_name='Adres Tarifi'),
        ),
        migrations.AddField(
            model_name='branches',
            name='photo',
            field=models.CharField(blank=True, help_text='Şubenin dıştan görüntüsünü ekleyiniz.', max_length=200, verbose_name='Şube Fotoğrafı'),
        ),
        migrations.AddField(
            model_name='sales',
            name='branch',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='finance.branches'),
        ),
        migrations.AlterField(
            model_name='branches',
            name='address',
            field=models.CharField(blank=True, help_text='Maksimum 300 karakter.', max_length=300, verbose_name='Adres'),
        ),
        migrations.AlterField(
            model_name='branches',
            name='author',
            field=models.ForeignKey(default=django.contrib.auth.models.User, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Yazar'),
        ),
        migrations.AlterField(
            model_name='branches',
            name='city',
            field=models.ForeignKey(blank=True, default=cities_light.models.Region, on_delete=django.db.models.deletion.CASCADE, to='cities_light.region', verbose_name='İl'),
        ),
        migrations.AlterField(
            model_name='branches',
            name='country',
            field=models.ForeignKey(blank=True, default=cities_light.models.Country, on_delete=django.db.models.deletion.CASCADE, to='cities_light.country', verbose_name='Ülke'),
        ),
        migrations.AlterField(
            model_name='branches',
            name='district',
            field=models.ForeignKey(blank=True, default=cities_light.models.SubRegion, on_delete=django.db.models.deletion.CASCADE, to='cities_light.subregion', verbose_name='İlçe'),
        ),
        migrations.AlterField(
            model_name='branches',
            name='email',
            field=models.CharField(blank=True, max_length=200, verbose_name='E-mail'),
        ),
        migrations.AlterField(
            model_name='branches',
            name='fri',
            field=models.CharField(blank=True, default='10:00 - 22:00', max_length=13, verbose_name='Cuma'),
        ),
        migrations.AlterField(
            model_name='branches',
            name='manager',
            field=models.CharField(blank=True, max_length=200, verbose_name='Şube Müdürü'),
        ),
        migrations.AlterField(
            model_name='branches',
            name='mon',
            field=models.CharField(blank=True, default='10:00 - 22:00', max_length=13, verbose_name='Pazartesi'),
        ),
        migrations.AlterField(
            model_name='branches',
            name='name',
            field=models.CharField(blank=True, help_text='AVM adını yazınız', max_length=200, verbose_name='Şube(AVM) Adı'),
        ),
        migrations.AlterField(
            model_name='branches',
            name='phone',
            field=models.CharField(blank=True, max_length=200, verbose_name='Telefon'),
        ),
        migrations.AlterField(
            model_name='branches',
            name='postcode',
            field=models.CharField(blank=True, help_text='Maksimum 5 karakterli sayı yazınız.', max_length=5, verbose_name='Posta Kodu'),
        ),
        migrations.AlterField(
            model_name='branches',
            name='sat',
            field=models.CharField(blank=True, default='10:00 - 22:00', max_length=13, verbose_name='Cumartesi'),
        ),
        migrations.AlterField(
            model_name='branches',
            name='sun',
            field=models.CharField(blank=True, default='10:00 - 22:00', max_length=13, verbose_name='Pazar'),
        ),
        migrations.AlterField(
            model_name='branches',
            name='thu',
            field=models.CharField(blank=True, default='10:00 - 22:00', max_length=13, verbose_name='Perşembe'),
        ),
        migrations.AlterField(
            model_name='branches',
            name='tue',
            field=models.CharField(blank=True, default='10:00 - 22:00', max_length=13, verbose_name='Salı'),
        ),
        migrations.AlterField(
            model_name='branches',
            name='wed',
            field=models.CharField(blank=True, default='10:00 - 22:00', max_length=13, verbose_name='Çarşamba'),
        ),
        migrations.AlterField(
            model_name='sales',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Kaydeden'),
        ),
        migrations.AlterField(
            model_name='sales',
            name='date',
            field=models.DateField(help_text='Lütfen tarihi belirtiniz.', verbose_name='Tarih'),
        ),
    ]
