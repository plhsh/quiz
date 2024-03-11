from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt # нужно обязательно это будет убрать. Отключает csrf проверку
from django.db.models import Q
from rbuilder.models import Locations, Links, Quotations
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from rbuilder.forms import QuotationsForm, CitiesQuotationsForm


def get_price(loc_1, loc_2, bandwidth):
    price = Links.objects.filter((Q(loc_1=loc_1) & Q(loc_2=loc_2) & Q(bandwidth=bandwidth)) |
                                       (Q(loc_1=loc_2) & Q(loc_2=loc_1) & Q(bandwidth=bandwidth))).first()
    return price



def add_quotation(request):
    if request.method == 'POST':
        try:
            f_addr_1 = request.POST.get('loc_1')
            f_addr_2 = request.POST.get('loc_2')

            loc_1 = Locations.objects.get(pk=f_addr_1)  # подтягиваем из запроса нужные данные
            loc_2 = Locations.objects.get(pk=f_addr_2)  # подтягиваем из запроса нужные данные

            print(loc_1)
            print(loc_2)

            bandwidth = request.POST.get('bandwidth')
            email = request.POST.get('email')

            price = get_price(loc_1, loc_2, bandwidth)  # подтягиваем из ORM выбранную цену
            print(price, "POST")

            lead = Quotations.objects.create(loc_1=loc_1, loc_2=loc_2, bandwidth=bandwidth, email=email)
            print(f"lead added to DB {lead}")

            return render(request, 'price.html', {'price': str(price)})
        except Exception as e:
            print(f"Ошибка: {e}")  # Логируем ошибку
            # Возвращаем сообщение об ошибке или перенаправляем на страницу с ошибкой
            return HttpResponse(f"Произошла ошибка при обработке вашего запроса.{e}  {price}", status=500)
    if request.method == 'GET':
        form = QuotationsForm()
        return render(request, 'quotation.html', {'form': form})


def add_quotation_cities(request):
    if request.method == 'POST':
        try:
            f_addr_1 = request.POST.get('loc_1')
            f_addr_2 = request.POST.get('loc_2')

            loc_1 = Locations.objects.get(pk=f_addr_1)  # подтягиваем из запроса нужные данные
            loc_2 = Locations.objects.get(pk=f_addr_2)  # подтягиваем из запроса нужные данные

            print(loc_1)
            print(loc_2)

            bandwidth = request.POST.get('bandwidth')
            email = request.POST.get('email')

            price = get_price(loc_1, loc_2, bandwidth)  # подтягиваем из ORM выбранную цену
            print(price, "POST")

            lead = Quotations.objects.create(loc_1=loc_1, loc_2=loc_2, bandwidth=bandwidth, email=email)
            print(f"lead added to DB {lead}")

            return render(request, 'price.html', {'price': str(price)})
        except Exception as e:
            print(f"Ошибка: {e}")  # Логируем ошибку
            # Возвращаем сообщение об ошибке или перенаправляем на страницу с ошибкой
            return HttpResponse(f"Произошла ошибка при обработке вашего запроса.{e}  {price}", status=500)
    if request.method == 'GET':
        form = CitiesQuotationsForm()
        return render(request, 'quotation.html', {'form': form})


# mock for tests
def show_price(request):
    price = '100500'
    return HttpResponse(price)


def index(request):
    return HttpResponse("Здесть ничего нет : )")