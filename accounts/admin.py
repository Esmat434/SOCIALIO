from django.contrib import admin
from .models import Country,State,City,Profile,Device
# Register your models here.

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ['id','name','abbr','is_enable','created_time']
    list_filter = ['name','abbr','is_enable']
    search_fields = ['name','abbr']

@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    list_display = ['id','country','name','is_enable']
    list_filter = ['name','is_enable']
    search_fields = ['name']

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ['id','state','name','is_enable']
    list_filter = ['name','is_enable']
    search_fields = ['name']

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['id','user','gender','phone_number','city','is_enable']
    list_filter = ['gender','is_enable']
    search_fields = ['user__username']

@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ['id','user','device_type','device_os','device_model','app_version']
    list_filter = ['device_type','device_os','device_model']
    search_fields = ['device_type','device_os','device_model']