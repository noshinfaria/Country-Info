from rest_framework import generics
from .models import Country
from .serializers import CountrySerializer

class CountryListView(generics.ListAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

