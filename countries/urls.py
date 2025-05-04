from django.urls import path
from .views import CountryListCreateAPIView, CountryDetailView

urlpatterns = [
    path('api/countries/', CountryListCreateAPIView.as_view(), name='country-list-create'),
    path('api/countries/<int:id>/', CountryDetailView.as_view(), name='country-detail'),
]
