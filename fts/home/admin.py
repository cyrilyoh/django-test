from django.contrib import admin
from .models import Car, Colour, OwnerRecord, Brand

# Register your models here.
admin.site.register(Colour)
admin.site.register(Brand)
admin.site.register(Car)
admin.site.register(OwnerRecord)