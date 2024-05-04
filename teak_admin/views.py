from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from utils.response import *
from teak_admin.serializers import BannerSerializer
from teak_admin.models import Banner


class BannerListCreateAPi(APIView):
    """API for list and create banner"""

    def get(self, request, *args, **kwargs):
        """API for list banner"""
        banner_instance = Banner.objects.all()
        banner_serializer = BannerSerializer(banner_instance, many=True)
        return HTTP_200({"banner": banner_serializer.data})

    def post(self, request, *args, **kwargs):
        """API for create banner"""
        banner_serializer = BannerSerializer(data=request.data)
        if not banner_serializer.is_valid():
            return HTTP_400({"error": banner_serializer.errors})
        banner_serializer.save()
        return HTTP_200(
            {"message": "banner created successfully", "banner": banner_serializer.data}
        )
