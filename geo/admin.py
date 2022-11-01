from django.contrib import admin
from .models import City, State, Country
# Register your models here.

class CityInline(admin.TabularInline):
    model = City
    extra: int = 1
    fields = ['name']

class StateInline(admin.TabularInline):
    model = State
    extra: int = 1
    fields = ['name']

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name']

@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name']
    class Meta:
        model = State
        fields = '__all__'
    inlines = [CityInline,]

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name']
    class Meta:
        modeld = Country
        fields = '__all__'
    inlines = [StateInline,]