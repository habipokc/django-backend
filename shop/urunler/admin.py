from django.contrib import admin
from .models import Kategoriler, Markalar, Urunler, Etiketler, Varyasyonlar


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

class InlineVaryasyon(admin.StackedInline):
    model = Varyasyonlar
    extra = 1

class UrunlerAdmin(admin.ModelAdmin):
    list_display = ['isim', 'fiyat', 'marka', 'kategori', 'aktifmi']
    list_filter = ['aktifmi', 'marka', 'kategori']
    search_fields = ['isim', 'seo_title', 'slug']
    inlines = [InlineVaryasyon]


admin.site.register(Urunler, UrunlerAdmin)

admin.site.register(Etiketler)

