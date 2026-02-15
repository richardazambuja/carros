from django import forms
from cars.models import Car, Brand
from decimal import Decimal

#Formulário antigo

#Formulário em uso
class CarModelForm(forms.ModelForm):
    
    value = forms.CharField()    
    
    class Meta:
        model = Car
        fields = '__all__'
        labels = {
            'model':'Modelo',
            'brand':'Marca',
            'factory_year':'Ano de Fabricação',
            'model_year':'Ano do Modelo',
            'plate':'Placa',
            'value':'Valor de Venda',
            'photo':'Foto',
            'bio':'Descrição'
        }

    def clean_value(self):
        value = self.cleaned_data.get('value')
        if value < 25000:
            self.add_error('value', 'Valor do carro deve ser de pelo menos R$25.000,00')
        return value

    def clean_factory_year(self):
        factory_year = self.cleaned_data.get('factory_year')
        if factory_year < 2015:
            self.add_error('factory_year', 'Nosso sistema só aceita carros fabricados a partir de 2015')
        return factory_year
    
    def clean_value(self):
        value = self.data.get('value')

        if value:
            value = value.replace('.', '').replace(',', '.')
            return Decimal(value)

        return None

    