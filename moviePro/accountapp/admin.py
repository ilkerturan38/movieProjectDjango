from django.contrib import admin
from .models import profile

class adminProfile(admin.ModelAdmin):
    list_display=['user',]

admin.site.register(profile,adminProfile)