from urunler.models import Kategoriler

def kategoriler(request):
    return {
        "menukategoriler": Kategoriler.objects.filter(menuden_goster=True).order_by("isim")
    }