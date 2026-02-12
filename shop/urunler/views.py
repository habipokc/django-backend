from django.shortcuts import render, get_object_or_404
from .models import Kategoriler, Markalar, Urunler, Etiketler


# Create your views here.

def anasayfa(request):
    urunler = Urunler.objects.filter(anasayfa=True)
    return render(request, "index.html", {"urunler": urunler})

def hakkinda(request):
    return render(request, "hakkinda.html")

def urundetay(request, slug):
    urun = get_object_or_404(Urunler, slug=slug)
    return render(request, "urun.html", {"urun": urun})


def kategoridetay(request, slug):
    kategori = get_object_or_404(Kategoriler, slug=slug)
    urunler = Urunler.objects.filter(kategori=kategori)
    return render(request, "kategori.html", {"kategori": kategori, "urunler": urunler})