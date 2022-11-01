from termios import CKILL
from django.db import models

# Create your models here.

class CountryManager(models.Manager):
    def add_country(self, name, id):
        country = self.create(name=name, country_id=id)
        return country

class StateManager(models.Manager):
    def add_state(self, name, id, country):
        state = self.create(name=name, state_id=id, country=country)
        return state


class CityManager(models.Manager):
    def add_city(self, name, id, state):
        city = self.create(name=name, city_id=id, state=state)
        return city

class Country(models.Model):
    name = models.CharField(max_length=50)
    country_id = models.IntegerField() 
    objects = CountryManager()

    def __str__(self) -> str:
        return self.name
    

class State(models.Model):
    name = models.CharField(max_length=50)
    state_id = models.IntegerField()
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='state', blank=True, null=True)
    objects = StateManager()

    def __str__(self) -> str:
        return self.name


class City(models.Model):
    name = models.CharField(max_length=90)
    city_id = models.IntegerField()
    state = models.ForeignKey(State, on_delete=models.CASCADE, related_name='city', blank=True, null=True)
    objects = CityManager()

    def __str__(self) -> str:
        return self.name
