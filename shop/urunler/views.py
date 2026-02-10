from django.shortcuts import render

# Create your views here.

def anasayfa(request):
    return render(request, "index.html")

def hakkinda(request):
    return render(request, "hakkinda.html")