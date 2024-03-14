from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.db.models import Q
from rbuilder.models import Locations, Links, Quotations, Cities
from django.urls import reverse_lazy
from rbuilder.forms import LocationsForm
import logging


logger = logging.getLogger('django')


def get_price(loc_1, loc_2, bandwidth):
    price = Links.objects.filter((Q(loc_1=loc_1) & Q(loc_2=loc_2) & Q(bandwidth=bandwidth)) |
                                       (Q(loc_1=loc_2) & Q(loc_2=loc_1) & Q(bandwidth=bandwidth))).first()
    return price


def add_quotation_cities(request):
    if request.method == 'POST':
        try:
            f_addr_1 = request.POST.get('address_a')
            f_addr_2 = request.POST.get('address_b')

            loc_1 = Locations.objects.get(pk=f_addr_1)  # подтягиваем из запроса нужные данные
            loc_2 = Locations.objects.get(pk=f_addr_2)  # подтягиваем из запроса нужные данные

            logger.debug(f"{loc_1}, {loc_2}")

            bandwidth = request.POST.get('bandwidth')
            email = request.POST.get('email')

            price = get_price(loc_1, loc_2, bandwidth)  # подтягиваем из ORM выбранную цену
            logger.debug(price)

            lead = Quotations.objects.create(loc_1=loc_1, loc_2=loc_2, bandwidth=bandwidth, email=email)
            logger.info(f"lead added to DB {lead}")

            return render(request, 'price.html', {'price': str(price)})
        except Exception as e:
            logger.error(f"Ошибка: {e}")  # Логируем ошибку
            # Возвращаем сообщение об ошибке или перенаправляем на страницу с ошибкой
            return HttpResponse(f"Произошла ошибка при обработке вашего запроса.{e}  {price}", status=500)
    if request.method == 'GET':
        form = LocationsForm()
        return render(request, 'quotation_cities.html', {'form': form})


def get_addresses(request):
    form = LocationsForm(request.GET)
    if request.META['HTTP_HX_TARGET'] == "id_address_a":
        return HttpResponse(form['address_a'])
    else:
        return HttpResponse(form['address_b'])


# mock for tests
def show_price(request):
    price = '100500'
    return HttpResponse(price)