import requests
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import NotFound
from django.shortcuts import render
from .models import Country
from .serializers import CountrySerializer

API_BASE = "http://localhost:8000/api/countries/"


class CountryListCreateAPIView(generics.ListCreateAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

class CountryRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    lookup_field = 'id'


class CountryDeleteAPIView(generics.DestroyAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    lookup_field = 'id'

    def destroy(self, request, *args, **kwargs):
        # Call the superclass's destroy method to delete the object
        response = super().destroy(request, *args, **kwargs)

        # After the object is deleted, add a custom message
        return Response({"detail": "Country deleted successfully."}, status=status.HTTP_204_NO_CONTENT)


class SameRegionCountriesAPIView(generics.ListAPIView):
    serializer_class = CountrySerializer

    def get_queryset(self):
        # Get the country id from the URL
        country_id = self.kwargs.get("id")
        country = Country.objects.get(id=country_id)

        # Filter countries by the same region
        return Country.objects.filter(region=country.region)
    
class CountrySearchAPIView(generics.ListAPIView):
    serializer_class = CountrySerializer

    def get_queryset(self):
        query = self.request.query_params.get('q', None)  # Get 'q' parameter for search query
        
        if query is None:
            raise NotFound(detail="Search query 'q' is required.")
        
        # Filter countries by name_common, case-insensitive and partial match
        return Country.objects.filter(name_official__icontains=query)






## For rendering HTML


def country_list_view(request):
    query = request.GET.get('q')
    if query:
        response = requests.get(f"{API_BASE}search/", params={'q': query})
    else:
        response = requests.get(API_BASE)
    
    data = response.json()
    countries = data.get("results", [])
    # print(countries)
    return render(request, 'countries/country_list.html', {'countries': countries})


def country_detail_view(request, id):
    country_response = requests.get(f"{API_BASE}{id}/")
    same_region_response = requests.get(f"{API_BASE}{id}/same-region/")

    if country_response.status_code == 404:
        return render(request, '404.html', status=404)

    country = country_response.json()
    data = same_region_response.json()
    same_region = data.get("results", [])
    print(same_region)
    return render(request, 'countries/country_detail.html', {
        'country': country,
        'same_region': same_region
    })
