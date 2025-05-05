import requests
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import NotFound
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Country
from .serializers import CountrySerializer

API_BASE = "http://localhost:8000/api/countries/"


class CountryListCreateAPIView(LoginRequiredMixin,generics.ListCreateAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

class CountryRetrieveUpdateAPIView(LoginRequiredMixin,generics.RetrieveUpdateAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    lookup_field = 'id'


class CountryDeleteAPIView(LoginRequiredMixin, generics.DestroyAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    lookup_field = 'id'

    def destroy(self, request, *args, **kwargs):
        # Call the superclass's destroy method to delete the object
        response = super().destroy(request, *args, **kwargs)

        # After the object is deleted, add a custom message
        return Response({"detail": "Country deleted successfully."}, status=status.HTTP_204_NO_CONTENT)


class SameRegionCountriesAPIView(LoginRequiredMixin, generics.ListAPIView):
    serializer_class = CountrySerializer

    def get_queryset(self):
        # Get the country id from the URL
        country_id = self.kwargs.get("id")
        country = Country.objects.get(id=country_id)

        # Filter countries by the same region
        return Country.objects.filter(region=country.region)
    
class CountriesByLanguageView(LoginRequiredMixin, generics.ListAPIView):
    serializer_class = CountrySerializer

    def get_queryset(self):
        language = self.request.query_params.get('q')
        if not language:
            return Country.objects.none()
        return Country.objects.filter(languages__icontains=language)

    def list(self, request, *args, **kwargs):
        language = request.query_params.get('q')
        if not language:
            return Response(
                {"error": "Language query parameter 'q' is required."},
                status=status.HTTP_400_BAD_REQUEST
            )

        queryset = self.get_queryset()
        if not queryset.exists():
            return Response(
                {"error": f"No countries found for language '{language}'."},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    
class CountrySearchAPIView(LoginRequiredMixin, generics.ListAPIView):
    serializer_class = CountrySerializer

    def get_queryset(self):
        query = self.request.query_params.get('q', None)  # Get 'q' parameter for search query
        
        if query is None:
            raise NotFound(detail="Search query 'q' is required.")
        
        # Filter countries by name_common, case-insensitive and partial match
        return Country.objects.filter(name_official__icontains=query)






## For rendering HTML

@login_required
def country_list_view(request):
    session = requests.Session()

    # Copy session cookies from Django request to the requests session
    for key, value in request.COOKIES.items():
        session.cookies.set(key, value)

    # Make the request to the internal API
    try:
        if query := request.GET.get('q'):
            response = session.get(f"{API_BASE}search/", params={'q': query})
        else:
            response = session.get(API_BASE)

        response.raise_for_status()

        data = response.json()
        countries = data.get("results", [])
    except Exception as e:
        print("Error fetching or decoding API response:", e)
        countries = []

    return render(request, 'countries/country_list.html', {'countries': countries})

@login_required
def country_detail_view(request, id):
    session = requests.Session()

    # Copy cookies from the Django request to the requests session
    for key, value in request.COOKIES.items():
        session.cookies.set(key, value)

    try:
        country_response = session.get(f"{API_BASE}{id}/")
        same_region_response = session.get(f"{API_BASE}{id}/same-region/")

        if country_response.status_code == 404:
            return render(request, '404.html', status=404)

        country = country_response.json()
        data = same_region_response.json()
        same_region = data.get("results", [])

        # Extract first language or fallback
        language = country.get("languages", [])[0].strip().lower() if country.get("languages") else ""
        # print(language)
        same_language_response = session.get(f"{API_BASE}language/?q={language}")
        data2 = same_language_response.json() if same_language_response.status_code == 200 else []
        same_language = data2 if isinstance(data2, list) else []
        # print(same_language)

    except Exception as e:
        print("Error fetching country detail:", e)
        country = {}
        same_region = []
        same_language = []

    return render(request, 'countries/country_detail.html', {
        'country': country,
        'same_region': same_region,
        'same_language': same_language
    })
