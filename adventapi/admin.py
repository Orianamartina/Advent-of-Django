from django.contrib import admin
from .models import Day, DayResolution,Reply, CustomUser
# Register your models here.
admin.site.register(Day)
admin.site.register(DayResolution)
admin.site.register(Reply)
admin.site.register(CustomUser)