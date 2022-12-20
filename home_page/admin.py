from django.contrib import admin

from . import models

admin.site.register(models.Menu)
admin.site.register(models.News)
admin.site.register(models.Chef)
admin.site.register(models.Branch)
admin.site.register(models.Review)
admin.site.register(models.Booking)
