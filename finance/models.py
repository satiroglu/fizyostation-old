import datetime

from django.db import models
from django.contrib.auth.models import User
from cities_light.models import *
from django.conf import settings

# Country, Region, City, SubRegion, ICity, ICountry, IRegion, ISubRegion


STATUS = (
    (0, "Aktif"),
    (1, "Pasif")
)

DEFAULTWORKINGHOURS = "10:00 - 22:00"

class Branches(models.Model):
    # Address Information
    country = models.ForeignKey(Country, on_delete=models.CASCADE, verbose_name="Ülke", default=Country )
    city = models.ForeignKey(Region, on_delete=models.CASCADE, verbose_name="İl", default=Region )
    district = models.ForeignKey(SubRegion, on_delete=models.CASCADE, verbose_name="İlçe", default=SubRegion )
    postcode = models.CharField(verbose_name="Posta Kodu", max_length=5, help_text='Maksimum 5 karakterli sayı yazınız.') # 34000
    address = models.CharField(verbose_name="Adres", max_length=300, help_text='Maksimum 300 karakter.')
    addressDescription = models.CharField(verbose_name="Adres Tarifi", max_length=300, help_text='Maksimum 300 karakter. Şubeye nasıl ulaşılabileceği hakkında bilgi yazın.')

    # Branch information
    name = models.CharField(verbose_name="Şube(AVM) Adı", max_length=200, help_text='AVM adını yazınız')
    photo = models.CharField(verbose_name="Şube Fotoğrafı", max_length=200, help_text='Şubenin dıştan görüntüsünü ekleyiniz.')

    # Contact Information
    manager = models.CharField(verbose_name="Şube Müdürü", max_length=200)
    phone = models.CharField(verbose_name="Telefon", max_length=200)
    email = models.CharField(verbose_name="E-mail", max_length=200)

    # Working hours
    mon = models.CharField(verbose_name="Pazartesi", max_length=13, default=DEFAULTWORKINGHOURS)
    tue = models.CharField(verbose_name="Salı", max_length=13, default=DEFAULTWORKINGHOURS)
    wed = models.CharField(verbose_name="Çarşamba", max_length=13, default=DEFAULTWORKINGHOURS)
    thu = models.CharField(verbose_name="Perşembe", max_length=13, default=DEFAULTWORKINGHOURS)
    fri = models.CharField(verbose_name="Cuma", max_length=13, default=DEFAULTWORKINGHOURS)
    sat = models.CharField(verbose_name="Cumartesi", max_length=13, default=DEFAULTWORKINGHOURS)
    sun = models.CharField(verbose_name="Pazar", max_length=13, default=DEFAULTWORKINGHOURS)

    # Other
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Yazar", default=User)
    createdOn = models.DateTimeField(verbose_name="Oluşturulma Tarihi", auto_now_add=True)
    updatedOn = models.DateTimeField(verbose_name="Güncellenme Tarihi", auto_now=True)
    status = models.IntegerField(verbose_name="Durum", choices=STATUS, default=0)

    class Meta:
        ordering = ['-createdOn']
        verbose_name = 'Şubeler'
        verbose_name_plural = 'Şubeler'

    def __str__(self):
        return self.name


class Sales(models.Model):
    # Sales information
    branch = models.ForeignKey(Branches, on_delete=models.CASCADE, default=1)
    date = models.DateField(verbose_name="Tarih", help_text="Lütfen tarihi belirtiniz.")
    credit = models.CharField(verbose_name="Kartlı Satış", max_length=200,
                              help_text='Kredi/Banka kartı ile post cihazı üzerinden yapılan satışların toplan tutarı')
    cash = models.CharField(verbose_name="Nakit Satış", max_length=200,)
    expense = models.SlugField(verbose_name="Gider", max_length=200,)
    remain = models.CharField(verbose_name="Kalan", max_length=200, default="headerPhoto")
    turnover = models.CharField(verbose_name="Ciro", max_length=200, default="headerPhoto")

    # Other
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Kaydeden")
    createdOn = models.DateTimeField(verbose_name="Oluşturulma Tarihi", auto_now_add=True)
    updatedOn = models.DateTimeField(verbose_name="Güncellenme Tarihi", auto_now=True)
    status = models.IntegerField(verbose_name="Durum", choices=STATUS, default=0)

    class Meta:
        ordering = ['-createdOn']
        verbose_name = 'Satışlar'
        verbose_name_plural = 'Satışlar'

    def __unicode__(self):
        return self.turnover

    # def __str__(self):
    #     return self.turnover
