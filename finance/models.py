from django.db import models
from django.contrib.auth.models import User

STATUS = (
    (0, "Aktif"),
    (1, "Pasif")
)


class Branches(models.Model):
    # Branch information
    name = models.CharField(verbose_name="Şube(AVM) Adı", max_length=200, unique=True, help_text='AVM adını yazınız')
    branchPhoto = models.CharField(verbose_name="Şube Fotoğrafı", max_length=200, unique=True, )

    # Contact Information
    manager = models.CharField(verbose_name="Şube Müdürü", max_length=200, unique=True)
    phone = models.CharField(verbose_name="Telefon", max_length=200, unique=True)
    email = models.CharField(verbose_name="E-mail", max_length=200, unique=True)

    # Address Information
    country = models.CharField(verbose_name="Ülke", max_length=200, unique=True)
    city = models.CharField(verbose_name="İl", max_length=200, unique=True)
    district = models.CharField(verbose_name="İlçe", max_length=200, unique=True)
    postcode = models.CharField(verbose_name="Posta Kodu", max_length=200)
    address = models.TextField(verbose_name="Adres", max_length=300, unique=True)
    description = models.TextField(verbose_name="Adres Tarifi")

    # Working hours
    mon = models.CharField(verbose_name="Pazartesi", max_length=200, unique=True, default="12:00 - 15:00")
    tue = models.CharField(verbose_name="Salı", max_length=200, unique=True, default="12:00 - 15:00")
    wed = models.CharField(verbose_name="Çarşamba", max_length=200, unique=True, default="12:00 - 15:00")
    thu = models.CharField(verbose_name="Perşembe", max_length=200, unique=True, default="12:00 - 15:00")
    fri = models.CharField(verbose_name="Cuma", max_length=200, unique=True, default="12:00 - 15:00")
    sat = models.CharField(verbose_name="Cumartesi", max_length=200, unique=True, default="12:00 - 15:00")
    sun = models.CharField(verbose_name="Pazar", max_length=200, unique=True, default="12:00 - 15:00")

    # Other
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Yazar", default=User.__name__)
    createdOn = models.DateTimeField(verbose_name="Oluşturulma Tarihi", auto_now_add=True)
    updatedOn = models.DateTimeField(verbose_name="Güncellenme Tarihi", auto_now=True)
    status = models.IntegerField(verbose_name="Durum", choices=STATUS, default=0)

    class Meta:
        ordering = ['-createdOn']
        verbose_name = 'Şube'
        verbose_name_plural = 'Şubeler'

    def __str__(self):
        return self.name


class Sales(models.Model):
    # Sales information
    date = models.CharField(verbose_name="Tarih", max_length=200, help_text="Lütfen tarihi belirtiniz.")
    credit = models.CharField(verbose_name="Kartlı Satış", max_length=200,
                              help_text='Kredi/Banka kartı ile post cihazı üzerinden yapılan satışların toplan tutarı')
    cash = models.CharField(verbose_name="Nakit Satış", max_length=200,)
    expense = models.SlugField(verbose_name="Gider", max_length=200,)
    remain = models.CharField(verbose_name="Kalan", max_length=200, default="headerPhoto")
    turnover = models.CharField(verbose_name="Ciro", max_length=200, default="headerPhoto")

    # SEO

    # Other
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Kaydeden", default=User.__name__, )
    createdOn = models.DateTimeField(verbose_name="Oluşturulma Tarihi", auto_now_add=True)
    updatedOn = models.DateTimeField(verbose_name="Güncellenme Tarihi", auto_now=True)
    status = models.IntegerField(verbose_name="Durum", choices=STATUS, default=0)

    class Meta:
        ordering = ['-createdOn']
        verbose_name = 'Satışlar1'
        verbose_name_plural = 'Satışlar1'

    def __unicode__(self):
        return self.date

    def __str__(self):
        return self.date
