from django.http import HttpResponse
from django.core import serializers
from django.http import HttpResponseRedirect
from main.forms import ProductForm
from django.urls import reverse
from main.models import Item

from django.shortcuts import render

def show_item(request):
    item = Item.objects.all()
    context = {
        'nama': 'Tengku Laras Malahayati',
        'kelas': 'PBP D',
        'items': item
    }

    return render(request, "main.html", context)

def create_product(request):
    '''Fungsi untuk mengembalikan data dalam bentuk HTML'''
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:create_product'))

    context = {'form': form}
    return render(request, "create_product.html", context)

def show_xml(request):
    '''Fungsi untuk mengembalikan data dalam bentuk XML'''
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    '''Fungsi untuk mengembalikan data dalam bentuk JSON'''
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    '''Fungsi untuk mengembalikan data dalam bentuk XML by ID'''
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    '''Fungsi untuk mengembalikan data dalam bentuk JSON by ID'''
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")