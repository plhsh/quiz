from django import forms
from rbuilder.models import Quotations, Locations, Cities
from dynamic_forms import DynamicField, DynamicFormMixin


class QuotationsForm(forms.ModelForm):
    loc_1 = forms.ModelChoiceField(queryset=Locations.objects.all(), label='Location A')
    loc_2 = forms.ModelChoiceField(queryset=Locations.objects.all(), label='Location B')
    bandwidth = forms.ChoiceField(choices=[(100, '100'), (1, '1'), (10, '10')], label='Speed')

    class Meta:
        model = Quotations
        fields = ['loc_1', 'loc_2', 'bandwidth', 'email']
        labels = {
            'email': 'Email'
        }


# Класс для кастомизации отображения элементов в выпадающем списке
# class CustomModelChoiceField(forms.ModelChoiceField):
#     def label_from_instance(self, obj):
#         # Возвращаем название города для каждого объекта
#         return obj.city
#
# class CitiesQuotationsForm(forms.ModelForm):
#     loc_1 = forms.ModelChoiceField(queryset=Cities.objects.all(), label='Локация 1')
#     loc_2 = CustomModelChoiceField(queryset=Locations.objects.all(), label='Локация 2')
#     bandwidth = forms.ChoiceField(choices=[(100, '100 Mbps'), (1, '1 Mbps'), (10, '10 Mbps')], label='Скорость')
#
#     class Meta:
#         model = Quotations
#         fields = ['loc_1', 'loc_2', 'bandwidth', 'email']
#         labels = {
#             'email': 'Email адрес'
#         }


class LocationsForm(DynamicFormMixin, forms.Form):

    def addresses_choices_a(self):
        city = self['city_a'].value()
        return Locations.objects.filter(ct=city)

    def addresses_choices_b(self):
        city = self['city_b'].value()
        return Locations.objects.filter(ct=city)

    cities_names = Cities.objects.all()

    city_a = forms.ModelChoiceField(queryset=cities_names,
                                    initial=cities_names[0],
                                    label="City A")
    city_b = forms.ModelChoiceField(queryset=cities_names,
                                    initial=cities_names[0],
                                    label="City B")

    address_a = DynamicField(
        forms.ModelChoiceField,
        queryset=addresses_choices_a,
        label="Address A"
    )

    address_b = DynamicField(
        forms.ModelChoiceField,
        queryset=addresses_choices_b,
        label="Address B"
    )

    bandwidth = forms.ChoiceField(choices=[(100, '100'), (1, '1'), (10, '10')], label='Speed')
    email = forms.EmailField(required=False, label='Email')

       # queryset=Locations.objects.filter(ct=self['city_a'].value())




    # class Meta:
    #     model = Cities
    #     fields = ['city_a']