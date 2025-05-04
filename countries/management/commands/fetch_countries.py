import requests
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = "Fetch country data from external API and store it in the database"

    def handle(self, *args, **kwargs):
        url = "https://restcountries.com/v3.1/all"
        response = requests.get(url)
        if response.status_code != 200:
            self.stderr.write("Failed to fetch data.")
            return

        data = response.json()
        print(data)
