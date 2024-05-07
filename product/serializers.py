from rest_framework import serializers
from product.models import *


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class SubCategorySerializers(serializers.ModelSerializer):
    category = CategorySerializers(read_only = True)
    class Meta:
        model = Subcategory
        fields = "__all__"
        

class SubofSubSerializers(serializers.ModelSerializer):
    sub_category = SubCategorySerializers(read_only = True)
    class Meta:
        model = SubofSub
        fields = "__all__"

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializers(read_only = True)
    class Meta:
        model = Product
        fields = "__all__"
        