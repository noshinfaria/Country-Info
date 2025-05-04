from django.urls import path
from .views import (
    CountryListCreateAPIView, 
    CountryRetrieveUpdateAPIView, 
    CountryDeleteAPIView, 
    SameRegionCountriesAPIView,
    CountrySearchAPIView
)

urlpatterns = [
    path('api/countries/', CountryListCreateAPIView.as_view(), name='country-list-create'),
    path('api/countries/<int:id>/', CountryRetrieveUpdateAPIView.as_view(), name='country-detail-update'),
    path('api/countries/<int:id>/delete/', CountryDeleteAPIView.as_view(), name='country-delete'),
    path('api/countries/<int:id>/same-region/', SameRegionCountriesAPIView.as_view(), name='same-region-countries'),
    path('api/countries/search/', CountrySearchAPIView.as_view(), name='country-search'),
]
