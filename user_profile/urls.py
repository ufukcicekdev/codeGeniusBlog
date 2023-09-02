from django.urls import path
from django.views.generic import TemplateView
from user_profile.views import login_user
from django.conf.urls import handler404, handler500
from .views import *


urlpatterns = [
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('register_user/', register_user, name='register_user'),
    path('profile/', profile, name='profile'),
    path('change_profile_picture/', change_profile_picture, name='change_profile_picture'),
    path('view_user_information/<str:username>/', view_user_information, name="view_user_information"),
    path('follow_or_unfollow/<int:user_id>/', follow_or_unfollow_user, name='follow_or_unfollow_user'),
    path('user_notifications/', user_notifications, name='user_notifications'),
    path('mute_or_unmute_user/<int:user_id>/', mute_or_unmute_user, name='mute_or_unmute_user'),
    path('robots.txt',TemplateView.as_view(template_name="robots.txt", content_type="text/plain")),

]

handler404 = 'user_profile.views.custom_404_view'
handler500 = 'user_profile.views.custom_500_view'
