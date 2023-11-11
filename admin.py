from django.contrib import admin
from . models import game,feeds
from myadmin.admin import Admin_site
# Register your models here.
admin.site.register(game)
admin.site.register(feeds)
Admin_site.register(game)
Admin_site.register(feeds)