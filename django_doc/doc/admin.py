from django.contrib import admin

from doc.models import Car, Manufacturer, User

admin.site.register(Car)
admin.site.register(Manufacturer)
admin.site.register(User)