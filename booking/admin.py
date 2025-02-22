from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.Table)
admin.site.register(models.BookedTable)
admin.site.register(models.BookedRoom)
admin.site.register(models.Room)
admin.site.register(models.Visitor)