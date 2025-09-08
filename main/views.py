from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2406495426',
        'name': 'Philo Pradipta Adhi Satriya',
        'class': 'PBP F'
    }

    return render(request, "main.html", context)
