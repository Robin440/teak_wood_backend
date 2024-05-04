from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from utils.response import *
from product.models import Category, Subcategory, SubofSub
from product.serializers import *


# Category API's


class CategoryListCreateAPI(APIView):
    """api for list and create category"""

    def get(self, request, *args, **kwargs):
        """api for list category"""
        category_instance = Category.objects.all()
        category_serializer = CategorySerializers(category_instance, many=True)
        return HTTP_200({"category": category_serializer.data})

    def post(self, request, *args, **kwargs):
        """api for post category"""

        category_serializer = CategorySerializers(data=request.data)
        if category_serializer.is_valid():
            category_serializer.save()
        else:
            return HTTP_400({"errors": category_serializer.errors})
        return HTTP_200(
            {
                "message": "category created successfully",
                "category": category_serializer.data,
            }
        )


class CategoryCRUDApi(APIView):
    """api for category crud"""

    def get(self, request, *args, **kwargs):
        """api for get category"""
        category_uuid = kwargs.get("category_uuid")
        if not category_uuid:
            return HTTP_400("Sorry! you have to provide category uuid")
        try:
            category_instance = Category.objects.get(uuid=category_uuid)
        except Category.DoesNotExist:
            return HTTP_400("Sorry! Category do not exists in database")
        category_serializer = CategorySerializers(category_instance)

        return HTTP_200({"category": category_serializer.data})

    def put(self, request, *args, **kwargs):
        """api for get category"""
        category_uuid = kwargs.get("category_uuid")
        if not category_uuid:
            return HTTP_400("Sorry! you have to provide category uuid")
        try:
            category_instance = Category.objects.get(uuid=category_uuid)
        except Category.DoesNotExist:
            return HTTP_400("Sorry! Category do not exists in database")
        category_serializer = CategorySerializers(
            instance=category_instance, data=request.data, partial=True
        )
        if category_serializer.is_valid():
            category_serializer.save()
        else:
            return HTTP_400({"error": category_serializer.errors})
        return HTTP_200(
            {
                "message": "category updated successfully",
                "category": category_serializer.data,
            }
        )

    def delete(self, request, *args, **kwargs):
        """api for delete category"""
        category_uuid = kwargs.get("category_uuid")
        if not category_uuid:
            return HTTP_400("Sorry! you have to provide category uuid")
        try:
            category_instance = Category.objects.get(uuid=category_uuid)
        except Category.DoesNotExist:
            return HTTP_400("Sorry! category do not found in database")
        category_instance.delete()
        return HTTP_200("Category deleted successfully")


# Sub category API's


class SubCategoryAPI(APIView):
    """api for list and create sub category"""

    def get(self, request, *args, **kwargs):
        """api for list sub category"""
        sub_category_instance = Subcategory.objects.all()
        sub_category_serializer = SubCategorySerializers(
            sub_category_instance, many=True
        )
        return HTTP_200({"sub_category": sub_category_serializer.data})

    def post(self, request, *args, **kwargs):
        """API for creating a subcategory"""
        sub_category_serializer = SubCategorySerializers(data=request.data)
        
        category_uuid = request.data.get("category")
        category = None
        
        if category_uuid:
            try:
                category = Category.objects.get(uuid=category_uuid)
            except Category.DoesNotExist:
                return HTTP_400("Category not found in the database")
        
        if sub_category_serializer.is_valid():
            sub_category_serializer.save(category=category)
            return HTTP_200({"message": "Subcategory created successfully", "sub_category": sub_category_serializer.data})
        else:
            return HTTP_400({"error": sub_category_serializer.errors})

class SubCategoryCRUDApi(APIView):
    """api for sub category CRUD"""

    def get(self, requst, *args, **kwargs):
        """api for sub get category"""
        sub_category_uuid = kwargs.get("sub_category_uuid")
        if not sub_category_uuid:
            return HTTP_400("Sorry! you have to provide sub category uuid")
        try:
            sub_category_instance = Subcategory.objects.get(uuid=sub_category_uuid)
        except Subcategory.DoesNotExist:
            return HTTP_400("Sorry! sub category is not found in database or deleted.")

        sub_category_serializer = SubCategorySerializers(sub_category_instance)

        return HTTP_200({"sub_category": sub_category_serializer.data})

    def put(self, request, *args, **kwargs):
        """api for sub get category"""
        sub_category_uuid = kwargs.get("sub_category_uuid")
        if not sub_category_uuid:
            return HTTP_400("Sorry! you have to provide sub category uuid")
        try:
            sub_category_instance = Subcategory.objects.get(uuid=sub_category_uuid)
        except Subcategory.DoesNotExist:
            return HTTP_400("Sorry! sub category is not found in database or deleted.")
        sub_category_serializer = SubCategorySerializers(
            instance=sub_category_instance, data=request.data, partial=True
        )
        if sub_category_serializer.is_valid():
            sub_category_serializer.save()
        else:
            return HTTP_400({"error": sub_category_serializer.errors})
        return HTTP_200(
            {
                "message": "category updated successfully",
                "category": sub_category_serializer.data,
            }
        )

    def delete(self, request, *args, **kwargs):
        """api for delete category"""
        sub_category_uuid = kwargs.get("sub_category_uuid")
        if not sub_category_uuid:
            return HTTP_400("Sorry! you have to provide sub category uuid")
        try:
            sub_category_instance = Subcategory.objects.get(uuid=sub_category_uuid)
        except Subcategory.DoesNotExist:
            return HTTP_400("Sorry! sub category do not found in database")
        sub_category_instance.delete()
        return HTTP_200("Sub Category deleted successfully")


# subs of subs


class SubofSubAPI(APIView):
    """api for subs of subs list and create"""

    def get(self, request, *args, **kwargs):
        """api for get subs of subs"""
        subs_instance = SubofSub.objects.all()
        subs_serializer = SubofSubSerializers(subs_instance, many=True)
        return HTTP_200({"subs_of": subs_serializer.data})

    def post(self, request, *args, **kwargs):
        """API for creating subcategories of subcategories"""
        subs_serializer = SubofSubSerializers(data=request.data)
        
        sub_category_uuid = request.data.get('sub_category')
        sub_category = None
        
        if sub_category_uuid:
            try:
                sub_category = Subcategory.objects.get(uuid=sub_category_uuid)
            except Subcategory.DoesNotExist:
                return HTTP_400("Sorry, subcategory not found in the database")
        
        if subs_serializer.is_valid():
            subs_serializer.save(sub_category=sub_category)
            return HTTP_200({"message": "Subs of subs created", "subs_of": subs_serializer.data})
        else:
            return HTTP_400({"error": subs_serializer.errors})

class SubsofSubsCRUDAPI(APIView):
    """api for subs crud operation"""

    def get(self, request, *args, **kwargs):
        """api for get subs"""
        subs_uuid = kwargs.get("subs_uuid")
        if not subs_uuid:
            return HTTP_400("Sorry! you have to provide subs of subs uuid")
        try:
            subs_instance = SubofSub.objects.get(uuid=subs_uuid)
        except SubofSub.DoesNotExist:
            return HTTP_400("Sorry! Subs of Subs is not found in database or deleted")
        subs_serializer = SubofSubSerializers(subs_instance)

        return HTTP_200({"subs_of": subs_serializer.data})

    def put(self, request, *args, **kwargs):
        """api for update subs"""
        subs_uuid = kwargs.get("subs_uuid")
        if not subs_uuid:
            return HTTP_400("Sorry! you have to provide subs of subs uuid")
        try:
            subs_instance = SubofSub.objects.get(uuid=subs_uuid)
        except SubofSub.DoesNotExist:
            return HTTP_400("Sorry! Subs of Subs is not found in database or deleted")
        subs_serializer = SubofSubSerializers(
            instance=subs_instance, data=request.data, partial=True
        )

        if subs_serializer.is_valid():
            subs_serializer.save()
        else:
            return HTTP_400({"error": subs_serializer.errors})
        return HTTP_200(
            {
                "message": "Subs of subs updated successfully",
                "subs_of": subs_serializer.data,
            }
        )

    def delete(self, request, *args, **kwargs):
        """api for delete subs"""
        subs_uuid = kwargs.get("subs_uuid")
        if not subs_uuid:
            return HTTP_400("Sorry! you have to provide subs of subs uuid")
        try:
            subs_instance = SubofSub.objects.get(uuid=subs_uuid)
        except SubofSub.DoesNotExist:
            return HTTP_400("Sorry! Subs of Subs is not found in database or deleted")
        subs_instance.delete()
        return HTTP_200("Subs of subs deleted successfully")


# products API's


class ProductsListCreateAPIview(APIView):
    """API for list create products"""

    def get(self, request, *args, **kwargs):
        """API for get products"""
        product_instance = Product.objects.all()

        product_serializer = productSerializer(product_instance, many=True)

        return HTTP_200({"product": product_serializer.data})

    def post(self,request,*args,**kwargs):
        """API for creating products"""
        product_serializer = productSerializer(data = request.data)
        category_uuid = request.data.get('category')
        category = None
        if category_uuid:
            try:
                category = Category.objects.get(uuid = category_uuid)
            except Category.DoesNotExist:
                return HTTP_400({"error":"Category not found in database"})
        if not product_serializer.is_valid():
            return HTTP_400({"error":product_serializer.errors})
        product_serializer.save(category = category)
        return HTTP_200({"message":"Product is created","product":product_serializer.data})
    
class ProductCRUDApi(APIView):
    """API for crud operation of products"""
    def get(self,request,*args,**kwargs):
        """API for get products"""
        product_uuid = kwargs.get('product_uuid')
        if not product_uuid:
            return HTTP_400({"error":"Sorry ! you need to provide product uuid"})
        try:
            product_instance = Product.objects.get(uuid = product_uuid)
        except Product.DoesNotExist:
            return HTTP_400({"error":"Sorry! product is not found in database or deleted"})
        product_serializer = productSerializer(product_instance)
        return HTTP_200({"product":product_serializer.data})


    def put(self,request,*args,**kwargs):
        """API for updating products"""
        product_uuid = kwargs.get('product_uuid')
        if not product_uuid:
            return HTTP_400({"error":"Sorry ! you need to provide product uuid"})
        try:
            product_instance = Product.objects.get(uuid = product_uuid)
        except Product.DoesNotExist:
            return HTTP_400({"error":"Sorry! product is not found in database or deleted"})
        category_uuid = request.data.get('category')
        catgeory = None
        if  category_uuid:
            try:
                category = Category.objects.get(uuid = category_uuid)
            except Category.DoesNotExist:
                return HTTP_400({"error":"Sorry! Category is not found in database or deleted"})
    
        product_serializer = productSerializer(instance= product_instance,data = request.data, partial = True)
        if not product_serializer.is_valid():
            return HTTP_400({"error":product_serializer.errors})
        product_serializer.save(category = category)
        return HTTP_200({"message":"Product is updated successfully","product":product_serializer.data})
        

    def delete(self,request,*args,**kwargs):
        """API for delete product"""

        product_uuid = kwargs.get('product_uuid')
        if not product_uuid:
            return HTTP_400({"error":"Sorry ! you need to provide product uuid"})
        try:
            product_instance = Product.objects.get(uuid = product_uuid)
        except Product.DoesNotExist:
            return HTTP_400({"error":"Sorry! product is not found in database or deleted"})
        product_instance.delete()
        return HTTP_200({"message":"Product deleted successfully"})