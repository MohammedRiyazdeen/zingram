from django.urls import path
from . import views

urlpatterns = [
    path('edit/', views.edit_profile, name='edit-profile'),

    # Profile view: /<username>/
    path('<str:username>/', views.profile_view, name='profile'),

    # Followers and Following list views:
    path('<str:username>/followers/', views.followers_list, name='followers-list'),
    path('<str:username>/following/', views.following_list, name='following-list'),

    # Follow/Unfollow action (POST only)
    path('<str:username>/follow/', views.follow_unfollow_view, name='follow-unfollow'),
]
