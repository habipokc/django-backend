from django.contrib import admin
from .models import Kategoriler

# Register your models here.

class KategoriAdmin(admin.ModelAdmin):
    list_display = ['isim', 'seo_title', 'slug', 'aktifmi']
    list_filter = ['aktifmi', 'isim']
    search_fields = ['isim', 'seo_title', 'slug']

admin.site.register(Kategoriler, KategoriAdmin)