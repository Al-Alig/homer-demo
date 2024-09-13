"""
This file is used to define the URL patterns for the user app.
"""
from django.urls import path
from django.contrib.auth import views as as_views
from . import views


urlpatterns = [
    path('signup/', views.signup),
    path('login/', as_views.LoginView.as_view()),
    path('logout/', as_views.LogoutView.as_view()),
    path('profile/', views.profile),
    path('profile/edit/', views.profile_edit, name='edit_profile'),
    path('user/<int:user_id>/', views.user_page, name='user')
]
