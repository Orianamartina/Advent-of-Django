from django.contrib import admin
from django.urls import path

from django.urls import path, include
from advent_days.days import day_1, day_2, day_3, day_4, day_5, day_6, day_7, day_8, day_9, day_10, day_11, day_12, day_13, day_14, day_15
from advent_days.views import solve_day, create_days

app_name = 'advent_days'

urlpatterns = [    
    # path('createdays/', create_days, name="create_days"),
    # path("solveday/<int:user_id>", solve_day, name="solve"),
]