from rest_framework import serializers
from rest_framework.serializers import SerializerMethodField
from .models import TinyUrl
from .logics import base_converter_from_base10


class TinyUrlSerializer(serializers.ModelSerializer):
    my_url = SerializerMethodField()

    class Meta:
        model = TinyUrl
        fields = ('my_url', 'url')

    def get_my_url(self, obj):
        return base_converter_from_base10(obj.my_url)



