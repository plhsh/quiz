from django import forms
from rbuilder.models import Quotations, Locations


class QuotationsForm(forms.ModelForm):
    loc_1 = forms.ModelChoiceField(queryset=Locations.objects.all(), label='Локация 1')
    loc_2 = forms.ModelChoiceField(queryset=Locations.objects.all(), label='Локация 2')
    bandwidth = forms.ChoiceField(choices=[(100, '100'), (1, '1'), (10, '10')], label='Скорость')

    class Meta:
        model = Quotations
        fields = ['loc_1', 'loc_2', 'bandwidth', 'email']
        labels = {
            'email': 'Email'
        }


# Класс для кастомизации отображения элементов в выпадающем списке
class CustomModelChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        # Возвращаем название города для каждого объекта
        return obj.city

class CitiesQuotationsForm(forms.ModelForm):
    loc_1 = CustomModelChoiceField(queryset=Locations.objects.all(), label='Локация 1')
    loc_2 = CustomModelChoiceField(queryset=Locations.objects.all(), label='Локация 2')
    bandwidth = forms.ChoiceField(choices=[(100, '100 Mbps'), (1, '1 Mbps'), (10, '10 Mbps')], label='Скорость')

    class Meta:
        model = Quotations
        fields = ['loc_1', 'loc_2', 'bandwidth', 'email']
        labels = {
            'email': 'Email адрес'
        }

