from django.shortcuts import render
from mywatchlist.models import WishlistFilmKu

from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def show_mywatchlist(request):
    data_barang_mywatchlist = WishlistFilmKu.objects.all()
    context ={
        'list_film': data_barang_mywatchlist,
        'nama': 'Afiq Ilyasa Akmal'
    }
    return render(request, "mywatchlist.html", context)

def show_xml(request):
    data = WishlistFilmKu.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = WishlistFilmKu.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

