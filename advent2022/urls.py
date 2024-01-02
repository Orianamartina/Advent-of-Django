
from django.contrib import admin
from django.urls import path, include
from adventapi.views import solve_day, create_days, get_user_days, home, submit_input
from adventapi.days import day_1, day_2, day_3, day_4, day_5, day_6, day_7
from django.views.generic.base import TemplateView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('createdays/', create_days, name="create_days"),
    path("accounts/", include("django.contrib.auth.urls")),
    path("", home, name="home"),
    path("submit", submit_input, name="submit"),
    path("resolutions/<int:user_id>", get_user_days, name="get_user_days"),
    path('day/1/<int:user_id>/', solve_day ,{'day_solve_function': day_1.solve, 'day': 1}, name="day_one"),
    path('day/2/<int:user_id>/', solve_day ,{'day_solve_function': day_2.solve, 'day': 2}, name="day_two"),
    path('day/3/<int:user_id>/', solve_day ,{'day_solve_function': day_3.solve, 'day': 3}, name="day_three"),
    path('day/4/<int:user_id>/', solve_day ,{'day_solve_function': day_4.solve, 'day': 4}, name="day_four"),
    path('day/5/<int:user_id>/', solve_day ,{'day_solve_function': day_5.solve, 'day': 5}, name="day_five"),
    path('day/6/<int:user_id>/', solve_day ,{'day_solve_function': day_6.solve, 'day': 6}, name="day_six"),
    path('day/7/<int:user_id>/', solve_day ,{'day_solve_function': day_7.solve, 'day': 7}, name="day_seven"),
]
