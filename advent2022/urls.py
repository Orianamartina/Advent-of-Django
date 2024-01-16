
from django.contrib import admin
from django.urls import path, include
from adventapi.views import solve_day, create_days, get_user_days, home, submit_input, signup, user_profile, resolution_code, save_comment, my_profile, upload_image, update_image_template_view
from adventapi.days import solve, day_1, day_2, day_3, day_4, day_5, day_6, day_7, day_8, day_9, day_10, day_11, day_12, day_13, day_14, day_15
urlpatterns = [
    path("__debug__/", include("debug_toolbar.urls")),
    path('admin/', admin.site.urls),
    path("", home, name="home"),
    path("profile/", my_profile, name="profile"),
    path('profile/<str:username>/', user_profile, name='user_profile'),
    path('code/<int:resolution_id>', resolution_code, name="resolution_code"),
    path("comment/<int:resolution_id>", save_comment, name="submit_reply"),
    path('createdays/', create_days, name="create_days"),
    path("accounts/", include("django.contrib.auth.urls")),
    path("signup/",signup , name='signup'),
    path("submit", submit_input, name="submit"),
    path("updateimage", update_image_template_view, name="update_image"),
    path("uploadimage/", upload_image, name="upload_image"),
    path("resolutions/<int:user_id>", get_user_days, name="get_user_days"),
    path("solveday/<int:user_id>", solve_day, name="solve"),
    path('day/1/<int:user_id>/', solve_day ,{'day_solve_function': day_1.solve, 'day': 1}, name="day_one"),
    path('day/2/<int:user_id>/', solve_day ,{'day_solve_function': day_2.solve, 'day': 2}, name="day_two"),
    path('day/3/<int:user_id>/', solve_day ,{'day_solve_function': day_3.solve, 'day': 3}, name="day_three"),
    path('day/4/<int:user_id>/', solve_day ,{'day_solve_function': day_4.solve, 'day': 4}, name="day_four"),
    path('day/5/<int:user_id>/', solve_day ,{'day_solve_function': day_5.solve, 'day': 5}, name="day_five"),
    path('day/6/<int:user_id>/', solve_day ,{'day_solve_function': day_6.solve, 'day': 6}, name="day_six"),
    path('day/7/<int:user_id>/', solve_day ,{'day_solve_function': day_7.solve, 'day': 7}, name="day_seven"),
    path('day/8/<int:user_id>/', solve_day ,{'day_solve_function': day_8.solve, 'day': 8}, name="day_eight"),
    path('day/9/<int:user_id>/', solve_day ,{'day_solve_function': day_9.solve, 'day': 9}, name="day_nine"),
    path('day/10/<int:user_id>/', solve_day ,{'day_solve_function': day_10.solve, 'day': 10}, name="day_ten"),
    path('day/11/<int:user_id>/', solve_day ,{'day_solve_function': day_11.solve, 'day': 11}, name="day_eleven"),
    path('day/12/<int:user_id>/', solve_day ,{'day_solve_function': day_12.solve, 'day': 12}, name="day_twelve"),
    path('day/13/<int:user_id>/', solve_day ,{'day_solve_function': day_13.solve, 'day': 13}, name="day_thirteen"),
    path('day/14/<int:user_id>/', solve_day ,{'day_solve_function': day_14.solve, 'day': 14}, name="day_fourteen"),
    path('day/15/<int:user_id>/', solve_day ,{'day_solve_function': day_15.solve, 'day': 15}, name="day_fifteen")

]
