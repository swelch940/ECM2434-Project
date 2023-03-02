#@authors Steven Welch, Luis Hidalgo

from django.urls import path, include
from . import views
from django.contrib import admin

urlpatterns = [
    path('', views.home, name='home'),
    path('map/', views.map, name='map'),
    path('leaderboard/', views.leaderboard, name="leaderboard"),
    path('admin/', admin.site.urls),
    path('register/', views.register, name="register"),
    path('tree', views.tree, name="tree"),
    path('', include("django.contrib.auth.urls")),
]
