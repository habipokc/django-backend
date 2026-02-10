from django.db import models

# Create your models here.

class Kategoriler(models.Model):
    isim = models.CharField(max_length=155)
    aktifmi = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'Kategoriler'
        verbose_name = 'Kategoriler'


    def __str__(self):
        return self.isim