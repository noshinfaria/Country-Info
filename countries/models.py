from django.db import models

class Country(models.Model):
    name_common = models.CharField(max_length=100)
    name_official = models.CharField(max_length=255)
    capital = models.CharField(max_length=100, blank=True, null=True)
    region = models.CharField(max_length=100, blank=True, null=True)
    subregion = models.CharField(max_length=100, blank=True, null=True)
    population = models.BigIntegerField(blank=True, null=True)
    area = models.FloatField(blank=True, null=True)
    flag_url = models.URLField(max_length=300, blank=True, null=True)

    def __str__(self):
        return self.name_common

