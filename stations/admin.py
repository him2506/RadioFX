from django.contrib import admin
from .models import Station
# Register your models here.

class StationAdmin(admin.ModelAdmin):
    list_display = ('station_name','station_id','category','state','Language','active')


admin.site.register(Station,StationAdmin)