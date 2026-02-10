from django.db import models

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