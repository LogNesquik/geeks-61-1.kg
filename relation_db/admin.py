from django.contrib import admin
from . import models

admin.site.register(models.NumberCar)
admin.site.register(models.DocumetsCar)
admin.site.register(models.Review)
admin.site.register(models.Tag)