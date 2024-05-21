from django.contrib.auth.models import  Group
from django.contrib import admin

# # Unregister the default ModelAdmin classes and register the custom ones

admin.site.unregister(Group)