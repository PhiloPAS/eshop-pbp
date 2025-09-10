from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'app_name' : 'FootyRetail',
        'name': 'Philo Pradipta Adhi Satriya',
        'kelas': 'PBP F'
    }

    return render(request, "main.html", context)
