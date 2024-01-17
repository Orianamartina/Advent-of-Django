from django.contrib import admin
from .models import Day, DayResolution,Comment, CustomUser, Language
# Register your models here.
admin.site.register(Day)
admin.site.register(DayResolution)
admin.site.register(Comment)
admin.site.register(CustomUser)
admin.site.register(Language)