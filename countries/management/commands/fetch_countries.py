import requests
from django.core.management.base import BaseCommand
from countries.models import Country

class Command(BaseCommand):
    help = "Fetch country data from API and store in the database"

    def handle(self, *args, **kwargs):
        url = "https://restcountries.com/v3.1/all"
        response = requests.get(url)

        if response.status_code != 200:
            self.stderr.write("Failed to fetch data.")
            return

        data = response.json()
        created_count = 0

        for item in data:
            name_common = item.get("name", {}).get("common")
            name_official = item.get("name", {}).get("official")
            capital = item.get("capital", [None])[0]
            region = item.get("region")
            subregion = item.get("subregion")
            population = item.get("population")
            area = item.get("area")
            flag_url = item.get("flags", {}).get("png")

            if name_common:  # Ensure we have a valid country name
                country, created = Country.objects.update_or_create(
                    name_common=name_common,
                    defaults={
                        "name_official": name_official,
                        "capital": capital,
                        "region": region,
                        "subregion": subregion,
                        "population": population,
                        "area": area,
                        "flag_url": flag_url,
                    }
                )
                if created:
                    created_count += 1

        self.stdout.write(self.style.SUCCESS(f"{created_count} countries stored/updated successfully."))

