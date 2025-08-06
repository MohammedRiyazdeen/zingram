from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_post_view, name='create_post'),
    path('feed/', views.feed_view, name='feed'),  # ✅ new feed route
]
