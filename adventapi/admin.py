from django.contrib import admin
from .models import Comment, CustomUser, Like
# Register your models here.

class LikeAdmin(admin.ModelAdmin):
    list_filter = ["user"]
    search_fields = ["user"]


admin.site.register(Comment)
admin.site.register(CustomUser)
admin.site.register(Like)