from django.urls import path
from .views import CountryListView

urlpatterns = [
    path('api/countries/', CountryListView.as_view(), name='country-list'),
]
