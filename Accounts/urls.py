# accounts/urls.py

from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    
    path('login/', views.login_view, name='login'),
    
    path('logout/', views.logout_view, name='logout'),

    
    path('register/', views.register_view, name='register'),

    
    path('profile/', views.profile_view, name='profile'),

    
    path('profile/edit/', views.edit_profile_view, name='edit_profile'),

    
    path('password/change/', views.password_change_view, name='password_change'),
]