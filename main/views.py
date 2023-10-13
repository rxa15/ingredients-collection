import datetime
from django.core import serializers
from django.urls import reverse
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages  
from main.forms import ProductForm
from main.models import Item

from django.shortcuts import render

@login_required(login_url='/login')

def show_item(request):
    item = Item.objects.filter(user=request.user)
    context = {
        'nama': request.user.username,
        'kelas': 'PBP D',
        'items': item,
        'last_login': request.COOKIES['last_login']
    }

    return render(request, "main.html", context)

def create_item(request):
    '''Fungsi untuk mengembalikan data dalam bentuk HTML'''
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        product = form.save(commit=False)
        product.user = request.user
        product.save()
        return HttpResponseRedirect(reverse('main:ingredients-collection'))
    context = {'form': form}
    return render(request, "create_item.html", context)

def register_account(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "You've successfully created your account!")
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register_account.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("main:ingredients-collection")) 
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

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

def increase_item(request, id):
    item = Item.objects.get(pk=id)
    item.amount += 1
    item.save()
    return HttpResponseRedirect(reverse('main:ingredients-collection'))

def decrease_item(request, id):
    item = Item.objects.get(pk=id)
    item.amount -= 1
    item.save()
    return HttpResponseRedirect(reverse('main:ingredients-collection'))

def delete(request, id):
    item = Item.objects.get(pk=id)
    item.delete()
    return HttpResponseRedirect(reverse('main:ingredients-collection'))

def get_item_json(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize('json', data))

# fungsi untuk menambahkan item baru ke basis data dengan AJAX
@csrf_exempt
def add_item_ajax(request):
    if request.method == 'POST':
        user = request.user
        name = request.POST.get("name")
        category = request.POST.get("category")
        amount = request.POST.get("amount")
        description = request.POST.get("amount")

        new_item = Item(user=user, name=name, category=category, amount=amount, description=description)
        new_item.save()
        return HttpResponse(b"CREATED", status = 201)
    return HttpResponseNotFound()