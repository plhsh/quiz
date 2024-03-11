from django.contrib import admin

from .models import Quotations, Locations, Links
admin.site.register(Quotations)
admin.site.register(Locations)
admin.site.register(Links)
