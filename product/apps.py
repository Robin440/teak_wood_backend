from django.apps import AppConfig


class ProductConfig(AppConfig):
    """for display name in admin panel"""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'product'
    verbose_name = "products and categories"
