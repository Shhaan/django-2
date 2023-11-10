from django.urls import path
from . import views
urlpatterns = [
    path('',views.myadminlogin,name='myadminlogin'),
    path('admin/',views.myadmin,name='myadmin'),
    path('admin/user',views.user,name='myuser'),
    path('admin/adminlogout',views.adminlogout,name='adminlogout'),
    path('admin/user/deleteuser',views.deleteuser,name='deleteuser'),
    path('admin/user/add',views.adduser,name='adduser'),
    path('admin/user/mysearch',views.mysearch,name='mysearch'),
    

]
