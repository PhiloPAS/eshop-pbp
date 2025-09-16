from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.core import serializers

from main.forms import ProductForm
from main.models import Product

# Serializers endpoints
def show_xml(request):
    product_list = Product.objects.all()
    xml_data = serializers.serialize("xml", product_list)
    return HttpResponse(xml_data, content_type="application/xml")

def show_json(request):
    product_list = Product.objects.all()
    json_data = serializers.serialize("json", product_list)
    return HttpResponse(json_data, content_type="application/json")

def show_xml_by_id(request, id):
    # gunakan filter agar hasilnya queryset (serializers.serialize butuh queryset/list)
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

# Main app views
def show_main(request):
    products = Product.objects.order_by('-created_at')[:30]
    context = {
        'app_name': 'FootyRetail',
        'name': 'Philo Pradipta Adhi Satriya',
        'kelas': 'PBP F',
        'products': products,
    }
    return render(request, "main.html", context)

def create_product(request):
    form = ProductForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect('main:show_main')
    return render(request, "create_product.html", {'form': form})

def show_product(request, id):
    product = get_object_or_404(Product, pk=id)
    # increment view counter (opsional)
    try:
        product.increment_views()
    except Exception:
        # jangan biarkan error kecil menghentikan rendering
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