from django.contrib import admin
from teak_admin.models import Banner

from django.utils.html import format_html
from django.contrib.admin import SimpleListFilter




class BannerAdmin(admin.ModelAdmin):
    """Class for category display customization""" 

    # add fields to diplay in user interface as list
    list_display = ('name', 'display_image','description')

    #pagination
    list_per_page = 5

    # function for display image
    def display_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="max-height: 100px; max-width: 100px;" />'.format(obj.image.url))
        return "No Image"

    display_image.allow_tags = True
    display_image.short_description = 'Image'  # Custom column header name 



# Register your models here.
admin.site.register(Banner,BannerAdmin)