from django.urls import path
from . import views
urlpatterns = [
    path('home/',views.home,name='home'),
    path('snake/',views.snake,name='snake'),
    path('flappy/',views.flappy,name='flappy'),
    path('feedback/',views.feedback,name='feedback'),
    path('about/',views.about,name='about'),
    path('',views.login,name='login'),
    path('register/',views.register,name='register'),
    path('logout',views.logout,name='logout'),
]
