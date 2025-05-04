from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import Country
from .serializers import CountrySerializer

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