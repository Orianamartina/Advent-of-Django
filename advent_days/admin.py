from django.contrib import admin
from .models import Day, DayResolution, Language
# Register your models here.

admin.site.register(Language)
admin.site.register(Day)
admin.site.register(DayResolution)