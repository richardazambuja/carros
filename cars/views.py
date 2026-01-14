from django.shortcuts import render, redirect
from cars.models import Car
from cars.forms import CarForm, CarModelForm
from django.views import View
from django.views.generic import ListView, CreateView

##FunctionBasedView
"""def car_view(request):
    cars = Car.objects.all().order_by('model')
    search = request.GET.get('search')

    if search:
        cars = cars.filter(model__icontains=search)
    

    return render (
        request,
        'cars.html',
        {'cars': cars}
    )"""


##Refatoração da FunctionBasedView no modelo ClassBasedView


class CarListView(ListView):
    model = Car
    template_name = 'cars.html'
    context_object_name = 'cars'

    def get_queryset(self):
        cars = super().get_queryset().order_by('model')
        search = self.request.GET.get('search')

        if search:
            cars = cars.filter(model__icontains=search)
        return cars






"""NewCarView herdando somente da classe View"""
"""class NewCarView(View):
    def get(self, request):
        if request.user.is_authenticated:
            new_car_form = CarModelForm()
            return render(request, 'new_car.html', {'new_car_form': new_car_form})

    def post(self, request):
        if request.user.is_authenticated:
            new_car_form = CarModelForm(request.POST, request.FILES)
            if new_car_form.is_valid():
                new_car_form.save()
                return redirect('cars_list')
            return render(request, 'new_car.html', {'new_car_form': new_car_form})
"""


class NewCarCreateView(CreateView):
    model = Car
    form_class = CarModelForm
    template_name = 'new_car.html'
    success_url = '/cars/'

class SucessView(View):
    def get(self, request):
        user = request.user 
        return render(request, 'sucess.html', )