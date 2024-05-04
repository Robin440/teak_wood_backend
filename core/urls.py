"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from product.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    # category urls
    path("api/category/", CategoryListCreateAPI.as_view(), name="category-list-create"),
    # category crud
    path(
        "api/category/<uuid:category_uuid>/",
        CategoryCRUDApi.as_view(),
        name="category-crud",
    ),
    # sub category urls
    path(
        "api/sub-category/", SubCategoryAPI.as_view(), name="sub-category-list-create"
    ),
    # sub category crud
    path(
        "api/sub-category/<uuid:sub_category_uuid>/",
        SubCategoryCRUDApi.as_view(),
        name="sub_category-crud",
    ),
    # subs of subs
    path("api/sub-of-sub/", SubofSubAPI.as_view(), name="subs-of-list-create"),
    # subs of subs crud
    path(
        "api/sub-of-sub/<uuid:subs_uuid>",
        SubsofSubsCRUDAPI.as_view(),
        name="subs-of-crud",
    ),
    # product urls
    path(
        "api/product/", ProductsListCreateAPIview.as_view(), name="product-list-create"
    ),
    # product crud
    path(
        "api/product/<uuid:product_uuid>/", ProductCRUDApi.as_view(), name="product-crud"
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
