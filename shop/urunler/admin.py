from django.contrib import admin
from .models import Kategoriler, Markalar, Urunler, Etiketler

# Register your models here.

class KategoriAdmin(admin.ModelAdmin):
    list_display = ['isim', 'seo_title', 'slug', 'aktifmi']
    list_filter = ['aktifmi', 'isim']
    search_fields = ['isim', 'seo_title', 'slug']

admin.site.register(Kategoriler, KategoriAdmin)

class MarkalarAdmin(admin.ModelAdmin):
    list_display = ['isim', 'seo_title', 'slug', 'aktifmi']
    list_filter = ['aktifmi', 'isim']
    search_fields = ['isim', 'seo_title', 'slug']

admin.site.register(Markalar, MarkalarAdmin)

class UrunlerAdmin(admin.ModelAdmin):
    list_display = ['isim', 'seo_title', 'slug', 'aktifmi']
    list_filter = ['aktifmi', 'isim']
    search_fields = ['isim', 'seo_title', 'slug']

admin.site.register(Urunler, UrunlerAdmin)

admin.site.register(Etiketler)