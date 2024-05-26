from rest_framework import serializers
from teak_admin.models import Banner


class BannerSerializer(serializers.ModelSerializer):
    """banner serializer"""
    class Meta:
        """meta class """
        model = Banner
        fields = "__all__"