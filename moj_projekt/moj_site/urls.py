from django.contrib import admin
from django.urls import path
from . import views
from sensor.views import sensor_view, register
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('login/',
         auth_views.LoginView.as_view(
             template_name='login.html'),
         name='login'),

    path('logout/',
         auth_views.LogoutView.as_view(),
         name='logout'),
    path('register/', register, name='register'),
    path('led/', views.led_index),
    path('led/on/', views.led_on),
    path('led/off/', views.led_off),

    path('sensor/', sensor_view),
]