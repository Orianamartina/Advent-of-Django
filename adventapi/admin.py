from django.contrib import admin
from .models import Day, DayResolution,Comment, CustomUser, Language, Like
# Register your models here.

class LikeAdmin(admin.ModelAdmin):
    list_filter = ["user"]
    search_fields = ["user"]



admin.site.register(Day)
admin.site.register(DayResolution)
admin.site.register(Comment)
admin.site.register(CustomUser)
admin.site.register(Language)
admin.site.register(Like)