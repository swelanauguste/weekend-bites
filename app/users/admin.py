from django.contrib import admin

from .models import Profile, User, Location

admin.site.register(Profile)
admin.site.register(User)
admin.site.register(Location)