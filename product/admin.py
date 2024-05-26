from django.contrib import admin

# Register your models here.

from product.models import Product, Category, Subcategory, SubofSub
from django.utils.html import format_html
from django.contrib.admin import SimpleListFilter
# from import_export.admin import ExportActionModelAdmin


class CategoryAdmin(admin.ModelAdmin):
    """Class for category display customization"""

    # add fields to diplay in user interface as list
    list_display = ("name", "display_image", "description")

    # pagination
    list_per_page = 5

    # function for display image
    def display_image(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="max-height: 100px; max-width: 100px;" />'.format(
                    obj.image.url
                )
            )
        return "No Image"

    display_image.allow_tags = True
    display_image.short_description = "Image"  # Custom column header name


admin.site.register(Category, CategoryAdmin)


class SubcategoryAdmin(admin.ModelAdmin):
    """Class for category display customization"""

    # add fields to diplay in user interface as list
    list_display = ("name", "display_image", "description", "category")

    # pagination
    list_per_page = 5

    # function for display image
    def display_image(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="max-height: 100px; max-width: 100px;" />'.format(
                    obj.image.url
                )
            )
        return "No Image"

    display_image.allow_tags = True
    display_image.short_description = "Image"  # Custom column header name


admin.site.register(Subcategory, SubcategoryAdmin)


class SubofSubcategoryAdmin(admin.ModelAdmin):
    """Class for category display customization"""

    # add fields to diplay in user interface as list
    list_display = ("name", "display_image", "description", "sub_category")

    # pagination
    list_per_page = 5

    # function for display image
    def display_image(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="max-height: 100px; max-width: 100px;" />'.format(
                    obj.image.url
                )
            )
        return "No Image"

    display_image.allow_tags = True
    display_image.short_description = "Image"  # Custom column header name


admin.site.register(SubofSub, SubofSubcategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    """Class for product display customization"""

    # add fields to diplay in user interface as list
    list_display = (
        "name",
        "display_image",
        "price",
        "qty",
        "category",
    )  # Add 'display_image' to list_display

    # pagination
    list_per_page = 5

    # search
    search_fields = ["name", "price", "category__name"]

    # sort and filter
    list_filter = ("category", "price", "qty", "material", "color", "created_at")

    fieldsets = [
        (
            "Product Information",
            {
                "fields": [
                    "name",
                    "description",
                    "price",
                    "qty",
                    "category",
                    "sold_by",
                    "material",
                    "brand",
                    "color",
                    "size",
                    "warranty",
                    "number_of_box",
                    "features",
                    "country_of_origin",
                    "is_featured",
                ]
            },
        ),
        (
            "Images",
            {
                "fields": [
                    "image_one",
                    "image_two",
                    "image_three",
                    "image_four",
                    "image_five",
                ]
            },
        ),
        ("Video", {"fields": ["video"]}),
    ]

    # function for display image
    def display_image(self, obj):
        if obj.image_one:
            return format_html('<img src="{}" style="max-height: 100px; max-width: 100px; border: 2px solid #0C4B33; border-radius: 10px; transition: border-color 0.3s;" onmouseover="this.style.borderColor=\'#00FF00\';" onmouseout="this.style.borderColor=\'#0C4B33\';" />'.format(obj.image_one.url))
        return "No Image"

    display_image.allow_tags = True
    display_image.short_description = "Image"  # Custom column header name


admin.site.register(Product, ProductAdmin)


admin.site.site_header = "Teakwood Factory"
admin.site.site_url = "https://teekwood-furniture.vercel.app"
