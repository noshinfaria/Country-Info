from django.urls import path
from .views import CountryListCreateAPIView, CountryRetrieveUpdateAPIView, CountryDeleteAPIView

urlpatterns = [
    path('api/countries/', CountryListCreateAPIView.as_view(), name='country-list-create'),
    path('api/countries/<int:id>/', CountryRetrieveUpdateAPIView.as_view(), name='country-detail-update'),
    path('api/countries/<int:id>/delete/', CountryDeleteAPIView.as_view(), name='country-delete'),
]
