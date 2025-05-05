import requests
from django.core.management.base import BaseCommand
from countries.models import Country, Currency


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
            if not name_common:
                continue

            country_defaults = {
                "name_official": item.get("name", {}).get("official"),
                "cca2": item.get("cca2"),
                "cca3": item.get("cca3"),
                "ccn3": item.get("ccn3"),
                "cioc": item.get("cioc"),
                "independent": item.get("independent", True),
                "un_member": item.get("unMember", True),
                "region": item.get("region"),
                "subregion": item.get("subregion"),
                "capital": item.get("capital", []),
                "area": item.get("area"),
                "population": item.get("population"),
                "landlocked": item.get("landlocked", False),
                "borders": item.get("borders", []),
                "timezones": item.get("timezones", []),
                "continents": item.get("continents", []),
                "flag_emoji": item.get("flag"),
                "flag_png": item.get("flags", {}).get("png"),
                "flag_svg": item.get("flags", {}).get("svg"),
                "coat_of_arms_png": item.get("coatOfArms", {}).get("png"),
                "coat_of_arms_svg": item.get("coatOfArms", {}).get("svg"),
                "start_of_week": item.get("startOfWeek", "monday"),
                "driving_side": item.get("car", {}).get("side", "right"),
                "capital_latlng": item.get("capitalInfo", {}).get("latlng"),
                "latlng": item.get("latlng"),
                "google_maps": item.get("maps", {}).get("googleMaps"),
                "open_street_maps": item.get("maps", {}).get("openStreetMaps"),
                "tlds": item.get("tld", []),
                "alt_spellings": item.get("altSpellings", []),
                "translations": item.get("translations", {}),
                "demonyms": item.get("demonyms", {}),
                "native_name": item.get("name", {}).get("nativeName", {}),
                "languages": list(item.get("languages", {}).values()),
                "gini": item.get("gini", {}),
                "postal_code": item.get("postalCode", {}),
                "idd": item.get("idd", {}),
            }

            country, created = Country.objects.update_or_create(
                cca3=item.get("cca3"), defaults=country_defaults
            )

            # Handle currencies
            currency_data = item.get("currencies", {})
            currency_instances = []
            for code, details in currency_data.items():
                currency, _ = Currency.objects.get_or_create(
                    code=code,
                    defaults={
                        "name": details.get("name"),
                        "symbol": details.get("symbol"),
                    },
                )
                currency_instances.append(currency)

            country.currencies.set(currency_instances)

            if created:
                created_count += 1

        self.stdout.write(self.style.SUCCESS(f"{created_count} countries stored/updated successfully."))
