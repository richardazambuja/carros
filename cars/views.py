from django.shortcuts import render


# Create your views here.
def car_view(request):
    return render (
        request,
        'cars.html',
        {'cars': {'model': 'Fiat Uno 1.0', 'ano': '1996'}}
    )
