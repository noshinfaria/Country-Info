from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import (
    CountryListCreateAPIView, 
    CountryRetrieveUpdateAPIView, 
    CountryDeleteAPIView, 
    SameRegionCountriesAPIView,
    CountriesByLanguageView,
    CountrySearchAPIView
)

urlpatterns = [
    path('api/countries/', CountryListCreateAPIView.as_view(), name='country-list-create'),
    path('api/countries/<int:id>/', CountryRetrieveUpdateAPIView.as_view(), name='country-detail-update'),
    path('api/countries/<int:id>/delete/', CountryDeleteAPIView.as_view(), name='country-delete'),
    path('api/countries/<int:id>/same-region/', SameRegionCountriesAPIView.as_view(), name='same-region-countries'),
    path('api/countries/language/', CountriesByLanguageView.as_view(), name='countries_by_language'),
    path('api/countries/search/', CountrySearchAPIView.as_view(), name='country-search'),
]

urlpatterns += [
    path('login/', auth_views.LoginView.as_view(template_name='countries/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('countries/', views.country_list_view, name='country_list_view'),
    path('countries/<int:id>/', views.country_detail_view, name='country_detail_view'),
]