from ast import Delete
import json
from os import path
from typing import Any, Optional
from django.core.management.base import BaseCommand, CommandParser
from geo.models import City, State, Country

class Command(BaseCommand):
    def add_arguments(self, parser: CommandParser):
        parser.add_argument('model', type=str)
        # return super().add_arguments(parser)

    def handle(self, *args: Any, **options: Any):
        json_path = options['model']
        print("jsonpath is ", json_path)
        print("type of json path is ", json_path)
        if json_path and path.exists(json_path):
            model = path.splitext(path.split(json_path)[-1])[0].capitalize()
            print("injesting data to ", model)
            
            if model == 'Cities' or model == 'City':
                self.inject_data_to_city(json_path)
            elif model == 'States' or model == 'State':
                self.inject_data_to_state(json_path)
            elif model == 'Countries' or model == 'Country':
                self.inject_data_to_country(json_path)
        else:
            print("Error: Json path doesn't exist or unreachable")
    
    def inject_data_to_city(self, path):
        cities = []
        with open(path, 'r') as f:
            cities = json.load(f)
        
        for city in cities:
            state_name = city["state_name"]
            country_name = city["country_name"]
            state_id = city["state_id"]
            city_id = city["id"]
            state = State.objects.get(name=state_name, state_id=state_id, country__name=country_name)

            city = City.objects.add_city(name=city["name"], id=city_id, state=state)

    
    def inject_data_to_state(self, path):
        states = []
        with open(path, 'r') as f:
            states = json.load(f)
        # State.objects.all().delete()
        
        for state in states:
            country_name = state["country_name"]
            country_id = state["country_id"]
            state_id = state["id"]

            country = Country.objects.get(name=country_name, country_id=country_id)
            State.objects.add_state(name=state["name"], id=state_id, country=country)


    def inject_data_to_country(self, path):
        countries = []
        with open(path, 'r') as f:
            countries = json.load(f)
        # Country.objects.all().delete()
        for country in countries:
            Country.objects.add_country(name=country["name"], id=country["id"])

        

