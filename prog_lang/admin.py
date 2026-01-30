from django.contrib import admin
from . import models

# регестрируем модель в админке
admin.site.register(models.ProgLang)

