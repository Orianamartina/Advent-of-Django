
from django.contrib import admin
from django.urls import path, include
from adventapi.views import submit_input, delete_day, get_user_days, home, signup, user_profile, resolution_code, save_comment, my_profile, upload_image, update_image_template_view, like_post,unlike_post
urlpatterns = [

    # path("", include("advent_days.urls")),
    # path("__debug__/", include("debug_toolbar.urls")),
    # path('admin/', admin.site.urls),
    # path("", home, name="home"),
    # path("profile/", my_profile, name="profile"),
    # path('profile/<str:username>/', user_profile, name='user_profile'),
    # path('code/<int:resolution_id>', resolution_code, name="resolution_code"),
    # path("comment/<int:resolution_id>", save_comment, name="submit_reply"),
    # path("accounts/", include("django.contrib.auth.urls")),
    # path("signup/",signup , name='signup'),
    # path("like/<int:post_id>", like_post, name="like post"), 
    # path("unlike/<int:post_id>", unlike_post, name="unlike post"),   
    # path("updateimage", update_image_template_view, name="update_image"),
    # path("uploadimage/", upload_image, name="upload_image"),
    # path("resolutions/<int:user_id>", get_user_days, name="get_user_days"),
    # path("deleteday/<int:day>", delete_day, name="delete day"),
    # path("submit", submit_input, name="submit"),
]
