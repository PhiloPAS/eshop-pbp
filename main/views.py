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

from django.http import HttpResponseRedirect, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.utils.html import strip_tags

import datetime

@csrf_exempt
@require_POST
def add_product_entry_ajax(request):
    name = strip_tags(request.POST.get("name"))
    description = strip_tags(request.POST.get("description"))
    category = request.POST.get("category")
    thumbnail = request.POST.get("thumbnail")
    price = request.POST.get("price", 0)
    stock = request.POST.get("stock", 0)
    is_featured = request.POST.get("is_featured") == 'true'
    user = request.user

    new_product = Product(
        name=name,
        description=description,
        price=price,
        stock=stock,
        category=category,
        thumbnail=thumbnail,
        is_featured=is_featured,
        user=user
    )
    new_product.save()

    return HttpResponse(b"CREATED", status=201)


def delete_product(request, id):
    product = get_object_or_404(Product, pk=id)
    product.delete()
    return HttpResponseRedirect(reverse('main:show_main'))

def edit_product(request, id):
    product = get_object_or_404(Product, pk=id)
    form = ProductForm(request.POST or None, instance=product)
    if form.is_valid() and request.method == 'POST':
        form.save()
        return redirect('main:show_main')
    context = {
        'form': form
    }
    return render(request, "edit_product.html", context)

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
    data = [
        {
            'id': str(product.id),
            'name': product.name,
            'description': product.description,
            'price': product.price,
            'stock': product.stock,
            'category': product.category,
            'thumbnail': product.thumbnail,
            'product_views': product.product_views,
            'created_at': product.created_at.isoformat() if product.created_at else None,
            'is_featured': product.is_featured,
            'user_id': product.user_id,
        }
        for product in product_list
    ]
    return JsonResponse(data, safe=False)

def show_xml_by_id(request, id):
    qs = Product.objects.filter(pk=id)
    if not qs.exists():
        return HttpResponse(status=404)
    xml_data = serializers.serialize("xml", qs)
    return HttpResponse(xml_data, content_type="application/xml")

def show_json_by_id(request, product_id):
    try:
        product = Product.objects.select_related('user').get(pk=product_id)
        data = {
            'id': str(product.id),
            'name': product.name,
            'description': product.description,
            'price': product.price,
            'stock': product.stock,
            'category': product.category,
            'thumbnail': product.thumbnail,
            'product_views': product.product_views,
            'created_at': product.created_at.isoformat() if product.created_at else None,
            'is_featured': product.is_featured,
            'user_id': product.user_id,
            'user_username': product.user.username if product.user_id else None,
            'user_fullname': product.user.get_full_name() if product.user_id else None,
        }
        return JsonResponse(data)
    except Product.DoesNotExist:
        return JsonResponse({'detail': 'Not found'}, status=404)

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