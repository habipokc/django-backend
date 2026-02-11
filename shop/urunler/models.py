from django.db import models
from django.db.models.fields import CharField
from django.contrib.auth.models import User
from django.utils.text import slugify

# Create your models here.

class Kategoriler(models.Model):
    isim = models.CharField(max_length=155)

    ustkategori = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True,
                   help_text='Eğer bu kategori başka bir kategoriye bağlıysa burayı doldurunuz')

    aktifmi = models.BooleanField(default=True)
    seo_title = models.CharField(max_length=155, blank=True, null=True)
    seo_description = models.TextField(blank=True, null=True)
    slug = models.SlugField(max_length=155, unique=True, null=True, blank=True)


    class Meta:
        verbose_name_plural = 'Kategoriler'
        verbose_name = 'Kategoriler'


    def __str__(self):
        return self.isim

class Markalar(models.Model):
    isim = CharField(max_length=155)
    aciklama = models.TextField(blank=True, null=True)
    seo_title = models.CharField(max_length=155, blank=True, null=True)
    seo_description = models.TextField(blank=True, null=True)
    slug = models.SlugField(max_length=155, unique=True, blank=True, null=True)
    aktifmi = models.BooleanField(default=True)
    resim = models.ImageField(upload_to="markaresimleri", blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Markalar'
        verbose_name = 'Marka'

    def __str__(self):
        return self.isim

class Etiketler(models.Model):
    isim = models.CharField(max_length=155)
    slug = models.SlugField(max_length=155, unique=True, blank=True, null=True)
    aktifmi = models.BooleanField(default=True)


class Urunler(models.Model):
    isim = CharField(max_length=155)
    kullanici = models.ForeignKey(User, on_delete=models.CASCADE)
    fiyat = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    marka = models.ForeignKey(Markalar, on_delete=models.CASCADE)
    kategori = models.ForeignKey(Kategoriler, on_delete=models.CASCADE)
    indirimli_fiyat = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    kisa_aciklama = models.TextField(blank=True, null=True)
    aciklama = models.TextField(blank=True, null=True)
    seo_title = models.CharField(max_length=155, blank=True, null=True)
    seo_description = models.TextField(blank=True, null=True)
    slug = models.SlugField(max_length=155, unique=True, blank=True, null=True)
    aktifmi = models.BooleanField(default=True)
    tarih = models.DateTimeField(auto_now_add=True)
    etiketler = models.ManyToManyField(Etiketler, blank=True)
    resim = models.ImageField(upload_to="urunresimleri", blank=True, null=True)
    anasayfa = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'Ürünler'
        verbose_name = 'Ürün'

    def __str__(self):
        return self.isim

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.isim)
            super(Urunler, self).save(*args, **kwargs)
        return self.slug

class Varyasyonlar(models.Model):
    urun = models.ForeignKey(Urunler, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    varyason = models.CharField(max_length=155, blank=True, null=True)
    fiyat = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    stok = models.IntegerField(blank=True, null=True)
    aktifmi = models.BooleanField(default=True)
    resim = models.ImageField(upload_to="varyasyonresimleri", blank=True, null=True)


    class Meta:
        verbose_name_plural = 'Varyasyonlar'
        verbose_name = 'Varyasyon'

    def __str__(self):
        return self.varyason or "Varyasyon"