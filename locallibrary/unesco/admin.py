from django.contrib import admin

# Register your models here.

from unesco.models import Site, Category, Name, Description, Justification, Year, Longitude, Latitude, AreaHectares, States, Region, ISO

admin.site.register(Site)
admin.site.register(Category)
admin.site.register(Name)
admin.site.register(Description)
admin.site.register(Justification)
admin.site.register(Year)
admin.site.register(Longitude)
admin.site.register(Latitude)
admin.site.register(AreaHectares)
admin.site.register(States)
admin.site.register(Region)
admin.site.register(ISO)