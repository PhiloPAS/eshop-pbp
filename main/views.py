from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required

from main.forms import ProductForm
from main.models import Product

import datetime

def register(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form': form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
    else:
        form = AuthenticationForm(request)
    context = {'form': form}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def show_xml(request):
    product_list = Product.objects.all()
    xml_data = serializers.serialize("xml", product_list)
    return HttpResponse(xml_data, content_type="application/xml")

def show_json(request):
    product_list = Product.objects.all()
    json_data = serializers.serialize("json", product_list)
    return HttpResponse(json_data, content_type="application/json")

def show_xml_by_id(request, id):
    qs = Product.objects.filter(pk=id)
    if not qs.exists():
        return HttpResponse(status=404)
    xml_data = serializers.serialize("xml", qs)
    return HttpResponse(xml_data, content_type="application/xml")

def show_json_by_id(request, id):
    qs = Product.objects.filter(pk=id)
    if not qs.exists():
        return HttpResponse(status=404)
    json_data = serializers.serialize("json", qs)
    return HttpResponse(json_data, content_type="application/json")

@login_required(login_url='/login')
def show_main(request):
    filter_type = request.GET.get("filter", "all")
    if filter_type == "all":
        qs = Product.objects.all()
    else:
        qs = Product.objects.filter(user=request.user)
    products = qs.order_by('-created_at')[:30]
    context = {
        'app_name': 'FootyRetail',
        'name': 'Philo Pradipta Adhi Satriya',
        'kelas': 'PBP F',
        'products': products,
        'last_login': request.COOKIES.get('last_login', 'Never'),
    }
    return render(request, "main.html", context)

@login_required(login_url='/login')
def create_product(request):
    form = ProductForm(request.POST or None, request.FILES or None)
    if request.method == 'POST' and form.is_valid():
        product = form.save(commit=False)
        product.user = request.user
        product.save()
        return redirect('main:show_main')
    context = {'form': form}
    return render(request, "create_product.html", context)

@login_required(login_url='/login')
def show_product(request, id):
    product = get_object_or_404(Product.objects.select_related('user'), pk=id)
    try:
        product.increment_views()
    except Exception:
        pass
    return render(request, "product_detail.html", {'product': product})




# janlup migrate lagi


# def add_employee(request):
    employee = Employee.objects.create(user_name="Zo", user_age=71, user_persona="Aku Suka PBP")
    context = {
        'user_name' : employee.user_name,
        'user_age' : employee.user_age,
        'user_persona' : employee.user_persona,
    }
    return render(request, "employee.html", context)

# employee.user_name, employee.user_age, employee.user_persona

# joe = Author.objects.create(name="Joe")
# clue: Employee.objects.create()
# clue2: Employee.objects.create(field1="abc", field2=123, ...)
# bernama add_employee, tujuannya menambah 1 employee. ketentuan: isi field name dgn nama kita, age bebas, persona bebas, dibikin routing urls.py 

# bikin html baru nge display employee