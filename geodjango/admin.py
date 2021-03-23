from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin
from .models import Person
from .models import Report
from .models import Entry

# Register your models here.

from leaflet.admin import LeafletGeoAdmin
from django.contrib import admin


@admin.register(Entry)
class EntryAdmin(OSMGeoAdmin):
    default_lon=-0.2472
    default_lat=35.2757
    default_zoom=6


class PersonAdmin(admin.ModelAdmin): 
    list_display = ('first_name','last_name')

class ReportAdmin(LeafletGeoAdmin):
    list_display = ('name','categories','location')    

admin.site.register(Person, PersonAdmin)
admin.site.register(Report, LeafletGeoAdmin)


