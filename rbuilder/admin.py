from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import Quotations, Locations, Links
admin.site.register(Quotations)
admin.site.register(Locations)

#
# class Loc1Filter(admin.SimpleListFilter):
#     title = _('City A')
#     parameter_name = 'loc_1'
#
#     def lookups(self, request, model_admin):
#         cities = set([c.city_id for c in model_admin.model.objects.all()])
#         return [(c.id, c.city) for c in cities]
#
#     def queryset(self, request, queryset):
#         if self.value():
#             return queryset.filter(loc_1__city_id__id=self.value())
#         return queryset
#
# class Loc2Filter(admin.SimpleListFilter):
#     title = _('City B')
#     parameter_name = 'loc_2'
#
#     def lookups(self, request, model_admin):
#         cities = set([c.city_id for c in model_admin.model.objects.all()])
#         return [(c.id, c.city) for c in cities]
#
#     def queryset(self, request, queryset):
#         if self.value():
#             return queryset.filter(loc_2__city_id__id=self.value())
#         return queryset


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
