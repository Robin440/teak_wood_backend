from django.shortcuts import render
from django.db.models import Q

# Create your views here.
from rest_framework.views import APIView
from utils.response import *
from product.models import Category, Subcategory, SubofSub
from product.serializers import *


# backend developed by robin rajan

# mob : 8086712029


# Category API's


class CategoryListCreateAPI(APIView):
    """api for list and create category"""

    def get(self, request, *args, **kwargs):
        """api for list category"""

        # query for list all category
        category_instance = Category.objects.all()

        # serialization of query
        category_serializer = CategorySerializers(category_instance, many=True)

        # success response
        return HTTP_200({"category": category_serializer.data})

    def post(self, request, *args, **kwargs):
        """api for post category"""

        # deserialization of json data to query
        category_serializer = CategorySerializers(data=request.data)

        # validating serializer 
        if category_serializer.is_valid():
            category_serializer.save()
        else:
            return HTTP_400({"errors": category_serializer.errors})
        
        # sucess response
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

        # receiving uuid 
        category_uuid = kwargs.get("category_uuid")
        # handling error in the absence of uuid
        if not category_uuid:
            return HTTP_400("Sorry! you have to provide category uuid")
        
        # query for category with error handling
        try:
            category_instance = Category.objects.get(uuid=category_uuid)
        except Category.DoesNotExist:
            return HTTP_400("Sorry! Category do not exists in database")
        
        # serialization
        category_serializer = CategorySerializers(category_instance)

        # success response
        return HTTP_200({"category": category_serializer.data})

    def put(self, request, *args, **kwargs):
        """api for get category"""

        # receiving uuid 
        category_uuid = kwargs.get("category_uuid")

        # handling error in the absence of uuid
        if not category_uuid:
            return HTTP_400("Sorry! you have to provide category uuid")
        
        # query for category with error handling
        try:
            category_instance = Category.objects.get(uuid=category_uuid)
        except Category.DoesNotExist:
            return HTTP_400("Sorry! Category do not exists in database")
        
        # deserialization
        category_serializer = CategorySerializers(
            instance=category_instance, data=request.data, partial=True
        )

        # validating serializer
        if category_serializer.is_valid():
            category_serializer.save()

        else:
            return HTTP_400({"error": category_serializer.errors})
        
        # success response
        return HTTP_200(
            {
                "message": "category updated successfully",
                "category": category_serializer.data,
            }
        )

    def delete(self, request, *args, **kwargs):
        """api for delete category"""

        # receiving uuid 
        category_uuid = kwargs.get("category_uuid")

        # handling error in the absence of uuid
        if not category_uuid:
            return HTTP_400("Sorry! you have to provide category uuid")
        

        # query for category with error handling
        try:
            category_instance = Category.objects.get(uuid=category_uuid)
        except Category.DoesNotExist:
            return HTTP_400("Sorry! category do not found in database")
        
        # deleting the instance 
        category_instance.delete()

        # success response 
        return HTTP_200("Category deleted successfully")


# Sub category API's

class SubCategoryAPI(APIView):
    """api for list and create sub category"""

    def get(self, request, *args, **kwargs):
        """api for list sub category"""

        # query for list all sub category and serialization 
        sub_category_instance = Subcategory.objects.all()
        sub_category_serializer = SubCategorySerializers(
            sub_category_instance, many=True
        )

        # success response
        return HTTP_200({"sub_category": sub_category_serializer.data})

    def post(self, request, *args, **kwargs):
        """API for creating a subcategory"""

        # deserialization
        sub_category_serializer = SubCategorySerializers(data=request.data)

        # receiving category uuid 
        category_uuid = request.data.get("category")
        category = None

        # validation and query for category
        if category_uuid:
            try:
                category = Category.objects.get(uuid=category_uuid)
            except Category.DoesNotExist:
                return HTTP_400("Category not found in the database")

        # validating serializer
        if sub_category_serializer.is_valid():
            sub_category_serializer.save(category=category)

            # success response
            return HTTP_200(
                {
                    "message": "Subcategory created successfully",
                    "sub_category": sub_category_serializer.data,
                }
            )
        
        return HTTP_400({"error": sub_category_serializer.errors})


class SubCategoryCRUDApi(APIView):
    """api for sub category CRUD"""

    def get(self, requst, *args, **kwargs):
        """api for sub get category"""

        # receiving sub category uuid
        sub_category_uuid = kwargs.get("sub_category_uuid")

        # error handling in the case of uuid absence
        if not sub_category_uuid:
            return HTTP_400("Sorry! you have to provide sub category uuid")
        
        # validating and query for sub category 
        try:
            sub_category_instance = Subcategory.objects.get(uuid=sub_category_uuid)
        except Subcategory.DoesNotExist:
            return HTTP_400("Sorry! sub category is not found in database or deleted.")

        # serialization
        sub_category_serializer = SubCategorySerializers(sub_category_instance)

        # success response
        return HTTP_200({"sub_category": sub_category_serializer.data})

    def put(self, request, *args, **kwargs):
        """api for sub get category"""

        # receiving sub category uuid
        sub_category_uuid = kwargs.get("sub_category_uuid")
        if not sub_category_uuid:
            return HTTP_400("Sorry! you have to provide sub category uuid")
        
        # validating and query for sub category
        try:
            sub_category_instance = Subcategory.objects.get(uuid=sub_category_uuid)
        except Subcategory.DoesNotExist:
            return HTTP_400("Sorry! sub category is not found in database or deleted.")
        
        # deserialization
        sub_category_serializer = SubCategorySerializers(
            instance=sub_category_instance, data=request.data, partial=True
        )

        # validation of serializer
        if sub_category_serializer.is_valid():
            sub_category_serializer.save()
        else:
            return HTTP_400({"error": sub_category_serializer.errors})
        
        # success response
        return HTTP_200(
            {
                "message": "category updated successfully",
                "category": sub_category_serializer.data,
            }
        )

    def delete(self, request, *args, **kwargs):
        """api for delete category"""

        # receiving uuid of sub category 
        sub_category_uuid = kwargs.get("sub_category_uuid")

        # error handling in the case of uuid
        if not sub_category_uuid:
            return HTTP_400("Sorry! you have to provide sub category uuid")
        
        # query and validation of sub category
        try:
            sub_category_instance = Subcategory.objects.get(uuid=sub_category_uuid)
        except Subcategory.DoesNotExist:
            return HTTP_400("Sorry! sub category do not found in database")
        
        # deletion of the instance from db 
        sub_category_instance.delete()

        # success response 
        return HTTP_200("Sub Category deleted successfully")


# subs of subs API's


class SubofSubAPI(APIView):
    """api for subs of subs list and create"""

    def get(self, request, *args, **kwargs):
        """api for get subs of subs"""

        # query for list all sub - sub category and serialization 
        subs_instance = SubofSub.objects.all()
        subs_serializer = SubofSubSerializers(subs_instance, many=True)

        # success response 
        return HTTP_200({"subs_of": subs_serializer.data})

    def post(self, request, *args, **kwargs):
        """API for creating subcategories of subcategories"""

        # deserialization
        subs_serializer = SubofSubSerializers(data=request.data)


        # assigning sub category uuid into a variable from request data
        sub_category_uuid = request.data.get("sub_category")
        sub_category = None


        # query and validating the sub category 
        if sub_category_uuid:
            try:
                sub_category = Subcategory.objects.get(uuid=sub_category_uuid)
            except Subcategory.DoesNotExist:
                return HTTP_400("Sorry, subcategory not found in the database")

        # validation of serializer and success response
        if subs_serializer.is_valid():
            subs_serializer.save(sub_category=sub_category)
            return HTTP_200(
                {"message": "Subs of subs created", "subs_of": subs_serializer.data}
            )
        
        return HTTP_400({"error": subs_serializer.errors})


class SubsofSubsCRUDAPI(APIView):
    """api for subs crud operation"""

    def get(self, request, *args, **kwargs):
        """api for get subs"""

        # receiving uuid
        subs_uuid = kwargs.get("subs_uuid")

        # error handling in the case of uuid absence
        if not subs_uuid:
            return HTTP_400("Sorry! you have to provide subs of subs uuid")
        
        # query for sub sub category and validating 
        try:
            subs_instance = SubofSub.objects.get(uuid=subs_uuid)
        except SubofSub.DoesNotExist:
            return HTTP_400("Sorry! Subs of Subs is not found in database or deleted")
        
        # serialization
        subs_serializer = SubofSubSerializers(subs_instance)

        # success response
        return HTTP_200({"subs_of": subs_serializer.data})

    def put(self, request, *args, **kwargs):
        """api for update subs"""

        # receiving uuid 
        subs_uuid = kwargs.get("subs_uuid")

        # error handling in the case of uuid absence 
        if not subs_uuid:
            return HTTP_400("Sorry! you have to provide subs of subs uuid")
        
        # query and validation of sub sub category uuid
        try:
            subs_instance = SubofSub.objects.get(uuid=subs_uuid)
        except SubofSub.DoesNotExist:
            return HTTP_400("Sorry! Subs of Subs is not found in database or deleted")
        
        # deserialization 
        subs_serializer = SubofSubSerializers(
            instance=subs_instance, data=request.data, partial=True
        )

        # validation of serializer
        if subs_serializer.is_valid():
            subs_serializer.save()
        else:
            return HTTP_400({"error": subs_serializer.errors})
        
        # success response 
        return HTTP_200(
            {
                "message": "Subs of subs updated successfully",
                "subs_of": subs_serializer.data,
            }
        )

    def delete(self, request, *args, **kwargs):
        """api for delete subs"""

        # receiving uuid 
        subs_uuid = kwargs.get("subs_uuid")

        # error handling in the case of uuid absence
        if not subs_uuid:
            return HTTP_400("Sorry! you have to provide subs of subs uuid")
        
        # query for sub sub category with error handling
        try:
            subs_instance = SubofSub.objects.get(uuid=subs_uuid)
        except SubofSub.DoesNotExist:
            return HTTP_400("Sorry! Subs of Subs is not found in database or deleted")
        
        # deletion of instance 
        subs_instance.delete()

        # success response 
        return HTTP_200("Subs of subs deleted successfully")


# products API's


class ProductsListCreateAPIview(APIView):
    """API for list create products"""

    def get(self, request, *args, **kwargs):
        """API for retrieving products with search functionality"""

        # Get the search query from the request parameters
        query = request.GET.get(
            "search"
        )  

        # code snippet for search
        if query:
            product_instance = Product.objects.filter(
                Q(name__icontains=query)
                | Q(description__icontains=query)
                | Q(category__name__icontains=query)
                | Q(category__subcategory__name__icontains=query)
                | Q(category__subcategory__subofsub__name__icontains=query)
            )
        else:
            product_instance = Product.objects.all()

        # serialization 
        product_serializer = ProductSerializer(product_instance, many=True)

        # success response 
        return HTTP_200({"products": product_serializer.data})

    def post(self, request, *args, **kwargs):
        """API for creating products"""

        # deserialization 
        product_serializer = ProductSerializer(data=request.data)

        # assigning category uuid to variable from request data
        category_uuid = request.data.get("category")
        category = None

        # query for category with error handling
        if category_uuid:
            try:
                category = Category.objects.get(uuid=category_uuid)
            except Category.DoesNotExist:
                return HTTP_400({"error": "Category not found in database"})
        # serializer validation 
        if not product_serializer.is_valid():
            return HTTP_400({"error": product_serializer.errors})
        
        product_serializer.save(category=category)

        # success response
        return HTTP_200(
            {"message": "Product is created", "product": product_serializer.data}
        )


class ProductCRUDApi(APIView):
    """API for crud operation of products"""

    def get(self, request, *args, **kwargs):
        """API for get products"""

        # receiving of product uuid 
        product_uuid = kwargs.get("product_uuid")

        # error handling in the case of uuid absence 
        if not product_uuid:
            return HTTP_400({"error": "Sorry ! you need to provide product uuid"})
        
        # query for product with error handling 
        try:
            product_instance = Product.objects.get(uuid=product_uuid)
        except Product.DoesNotExist:
            return HTTP_400(
                {"error": "Sorry! product is not found in database or deleted"}
            )
        
        # serialization 
        product_serializer = ProductSerializer(product_instance)

        # success response 
        return HTTP_200({"product": product_serializer.data})

    def put(self, request, *args, **kwargs):
        """API for updating products"""

        # receiving uuid of product
        product_uuid = kwargs.get("product_uuid")

        # error handling in the case of uuid absence 
        if not product_uuid:
            return HTTP_400({"error": "Sorry ! you need to provide product uuid"})
        
        # query for product with error handling
        try:
            product_instance = Product.objects.get(uuid=product_uuid)
        except Product.DoesNotExist:
            return HTTP_400(
                {"error": "Sorry! product is not found in database or deleted"}
            )
        
        # assigning category uuid to variable
        category_uuid = request.data.get("category")
        category = None

        # query for category with error handling 
        if category_uuid:
            try:
                category = Category.objects.get(uuid=category_uuid)
            except Category.DoesNotExist:
                return HTTP_400(
                    {"error": "Sorry! Category is not found in database or deleted"}
                )

        # deserialization
        product_serializer = ProductSerializer(
            instance=product_instance, data=request.data, partial=True
        )

        # validation of serializer
        if not product_serializer.is_valid():
            return HTTP_400({"error": product_serializer.errors})
        product_serializer.save(category=category)

        # success response
        return HTTP_200(
            {
                "message": "Product is updated successfully",
                "product": product_serializer.data,
            }
        )

    def delete(self, request, *args, **kwargs):
        """API for delete product"""

        # receiving product uuid
        product_uuid = kwargs.get("product_uuid")

        # error handling in the case of uuid absence
        if not product_uuid:
            return HTTP_400({"error": "Sorry ! you need to provide product uuid"})
        
        # query for product with error handling
        try:
            product_instance = Product.objects.get(uuid=product_uuid)
        except Product.DoesNotExist:
            return HTTP_400(
                {"error": "Sorry! product is not found in database or deleted"}
            )
        
        # deletion of product instance
        product_instance.delete()

        # success response 
        return HTTP_200({"message": "Product deleted successfully"})


# separate api for search products 
class SearchProductAPI(APIView):
    """API for search products"""

    def get(self, request, *args, **kwargs):
        """API for search products"""

        # receiving query and assigning value to variable
        query = request.GET.get("search")

        # return error if not search query
        if not query:
            return HTTP_400({"error": "Sorry! you need to provide search query"})
        
        # filtering query in db
        product_instance = Product.objects.filter(
                Q(name__icontains=query)
                | Q(description__icontains=query)
                | Q(category__name__icontains=query)
                | Q(category__subcategory__name__icontains=query)
                | Q(category__subcategory__subofsub__name__icontains=query)
            )

        # serializing the query
        product_serializer = ProductSerializer(product_instance,many = True)

        return HTTP_200({'product':product_serializer.data})




# backend developed by robin rajan

# mob : 8086712029
