from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.db.models import JSONField

class Currency(models.Model):
    code = models.CharField(max_length=3, primary_key=True)
    name = models.CharField(max_length=100)
    symbol = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.name} ({self.symbol})"

class Country(models.Model):
    name_common = models.CharField(max_length=100)
    name_official = models.CharField(max_length=150)
    cca2 = models.CharField(max_length=2, unique=True)
    cca3 = models.CharField(max_length=3, unique=True)
    ccn3 = models.CharField(max_length=3, unique=True)
    cioc = models.CharField(max_length=3, null=True, blank=True)
    independent = models.BooleanField(default=True)
    un_member = models.BooleanField(default=True)
    region = models.CharField(max_length=100)
    subregion = models.CharField(max_length=100, null=True, blank=True)

    capital = models.JSONField(default=list)
    area = models.FloatField()
    population = models.BigIntegerField()
    landlocked = models.BooleanField(default=False)
    borders = models.JSONField(default=list, blank=True)
    timezones = models.JSONField(default=list)
    continents = models.JSONField(default=list)

    flag_emoji = models.CharField(max_length=10)
    flag_png = models.URLField()
    flag_svg = models.URLField()

    coat_of_arms_png = models.URLField(null=True, blank=True)
    coat_of_arms_svg = models.URLField(null=True, blank=True)

    start_of_week = models.CharField(max_length=10, default='monday')
    driving_side = models.CharField(max_length=10, default='right')

    capital_latlng = models.JSONField(null=True, blank=True)
    latlng = models.JSONField(null=True, blank=True)

    google_maps = models.URLField()
    open_street_maps = models.URLField()

    tlds = models.JSONField(default=list)
    alt_spellings = models.JSONField(default=list)

    currencies = models.ManyToManyField(Currency, blank=True)

    translations = models.JSONField(default=dict)
    demonyms = models.JSONField(default=dict)
    native_name = models.JSONField(default=dict)
    languages = models.JSONField(default=list)
    gini = models.JSONField(default=dict)
    postal_code = models.JSONField(default=dict)
    idd = models.JSONField(default=dict)


    def __str__(self):
        return self.name_common


