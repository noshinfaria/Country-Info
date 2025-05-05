from django.contrib import admin
from .models import Country

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ("name_official", "capital", "region", "population")
    search_fields = ("name_official", "capital", "region")

