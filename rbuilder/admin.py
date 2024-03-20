from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import Quotations, Locations, Links
admin.site.register(Quotations)
admin.site.register(Locations)


@admin.register(Links)
class LinksAdmin(admin.ModelAdmin):
    list_display = ['id', 'get_loc_1', 'loc_1', 'get_loc_2', 'loc_2', 'bandwidth', 'price']
    list_editable = ['price']
    list_filter = [
        ('loc_1', admin.RelatedOnlyFieldListFilter),
        ('loc_2', admin.RelatedOnlyFieldListFilter)
    ]


    @staticmethod
    @admin.display(description="City A")
    def get_loc_1(link: Links):
        return link.loc_1.city_id

    @staticmethod
    @admin.display(description="City B")
    def get_loc_2(link: Links):
        return link.loc_2.city_id
