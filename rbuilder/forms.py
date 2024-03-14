from django import forms
from rbuilder.models import Locations, Cities
from dynamic_forms import DynamicField, DynamicFormMixin


class LocationsForm(DynamicFormMixin, forms.Form):

    def addresses_choices_a(self):
        city = self['city_a'].value()
        return Locations.objects.filter(city_id=city)

    def addresses_choices_b(self):
        city = self['city_b'].value()
        return Locations.objects.filter(city_id=city)

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


class AddressForm(forms.Form):
    address = forms.ChoiceField()

    def __init__(self, *args, **kwargs):
        super(AddressForm, self).__init__(*args, **kwargs)
        choices = [('', 'Выберите адрес...')]

        for c in Cities.objects.all():
            city_options = [(a.pk, f"--- {a.address}") for a in c.addresses_by_city.all()]
            if city_options:
                choices.append((c.city, city_options))

        self.fields['address'].choices = choices
