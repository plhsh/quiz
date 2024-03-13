"""
URL configuration for nextr project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from rbuilder import views

urlpatterns = [
    path("__debug__/", include("debug_toolbar.urls")),
    path('admin/', admin.site.urls),
    path('', views.add_quotation_cities, name='add_quotation_cities'),
    path('simple-choices/', views.add_quotation, name='add_quotation'),
    path('get_addresses/', views.get_addresses, name='get_addresses'),
    path('price/', views.show_price, name='price') # mock for tests

]

