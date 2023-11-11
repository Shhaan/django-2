from django.contrib import admin
from .models import dumy
# Register your models here.
class MyAdminSite(admin.AdminSite):
    site_header = 'My Custom Admin Site'  
    site_title = 'My Admin Site'
Admin_site = MyAdminSite(name='My_Admin')

 
Admin_site.register(dumy)
admin.site.register(dumy)