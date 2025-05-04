from django.urls import path
from .views import CountryListView, CountryDetailView

urlpatterns = [
    path('api/countries/', CountryListView.as_view(), name='country-list'),
    path('api/countries/<int:id>/', CountryDetailView.as_view(), name='country-detail'),
]
