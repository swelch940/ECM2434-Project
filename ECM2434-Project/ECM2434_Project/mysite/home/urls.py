from django.urls import path, include
from . import views
from django.contrib import admin
#from .views import leaderboardView

urlpatterns = [
    path('', views.home, name='home'),
    path('map/', views.map, name='map'),
    path('leaderboard/', views.leaderboard, name="leaderboard"),
    path('about/', views.about, name="about"),
    path('admin/', admin.site.urls),
    path('register/', views.register, name="register"),
    path('tree', views.tree, name="tree"),
    path('settings/', views.settings, name="settings"),
    #path('leaderboard', leaderboardView, name='leaderboard'),
    path('deleteaccount/', views.deleteaccount, name="deleteaccount"),
    path('bottlesize/', views.bottlesize, name="bottlesize"),
    path('newpassword/', views.newpassword, name="newpassword"),
    path('newemail/', views.newemail, name="newemail"),
    path('tree/', views.tree, name="tree"),  
    path('', include("django.contrib.auth.urls")),
]