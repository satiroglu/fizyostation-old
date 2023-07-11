import readline

from django.db import models
from django.contrib.auth.models import User

STATUS = (
    (0, "Aktif"),
    (1, "Pasif")
)

LANGUAGE = (
    (0, "Türkçe"),
    (1, "English"),
    (2, "German"),
    (3, "French"),
    (4, "Spanish")

)

CURRENCY = (
    (0, "TRY"),
    (1, "USD"),
    (2, "EURO"),
    (3, "GBP")
)


class Page(models.Model):
    # Page information
    pageTitle = models.CharField(verbose_name="Sayfa Başlığı", max_length=200, unique=True)
    menuTitle = models.CharField(verbose_name="Menü Başlığı", max_length=200, unique=True)
    slug = models.SlugField(verbose_name="Slug", max_length=200, unique=True)
    featuredPhoto = models.CharField(verbose_name="Öne Çıkan Görsel", max_length=200, unique=True,
                                     default="headerPhoto")
    content = models.TextField(verbose_name="İçerik")

    # SEO

    # Other
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Yazar", default=User.__name__, )
    createdOn = models.DateTimeField(verbose_name="Oluşturulma Tarihi", auto_now_add=True)
    updatedOn = models.DateTimeField(verbose_name="Güncellenme Tarihi", auto_now=True)
    status = models.IntegerField(verbose_name="Durum", choices=STATUS, default=0)

    class Meta:
        ordering = ['-createdOn']
        verbose_name = 'Sayfa'
        verbose_name_plural = 'Sayfalar'

    def __str__(self):
        return self.pageTitle


class Branch(models.Model):
    # Branch information
    name = models.CharField(verbose_name="Şube Adı", max_length=200, unique=True, help_text='AVM adını yazınız')
    headerPhoto = models.CharField(verbose_name="Header Photo", max_length=200, unique=True, default="headerPhoto")
    description = models.TextField(verbose_name="Açıklama")
    website = models.CharField(verbose_name="Websitesi", max_length=200, unique=True,
                               default="https://www.digirest.co.uk/")
    email = models.CharField(verbose_name="E-mail", max_length=200, unique=True)
    phone = models.CharField(verbose_name="Telefon", max_length=200, unique=True)
    address = models.CharField(verbose_name="Adres", max_length=300, unique=True)
    postcode = models.CharField(verbose_name="Posta Kodu", max_length=200, unique=True)
    district = models.CharField(verbose_name="İlçe", max_length=200, unique=True)
    city = models.CharField(verbose_name="Şehir", max_length=200, unique=True)
    country = models.CharField(verbose_name="Ülke", max_length=200, unique=True)

    # Social
    facebook = models.CharField(verbose_name="Facebook", max_length=200, unique=True)
    instagram = models.CharField(verbose_name="Instagram", max_length=200, unique=True)
    youtube = models.CharField(verbose_name="YouTube", max_length=200, unique=True)
    twitter = models.CharField(verbose_name="Twitter", max_length=200, unique=True)
    linkedin = models.CharField(verbose_name="LinkedIn", max_length=200, unique=True)
    pinterest = models.CharField(verbose_name="Pinterest", max_length=200, unique=True)
    tripadvisor = models.CharField(verbose_name="TripAdvisor", max_length=200, unique=True)
    telegram = models.CharField(verbose_name="Telegram", max_length=200, unique=True)
    whatsapp = models.CharField(verbose_name="WhatsApp", max_length=200, unique=True)

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
