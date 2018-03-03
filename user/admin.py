from django.contrib import admin
from user.models import *


# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user')


admin.site.register(Profile, ProfileAdmin)
