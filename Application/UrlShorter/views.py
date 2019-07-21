from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework import viewsets
from .models import TinyUrl
from .Serializers import TinyUrlSerializer


def index(request):
    return HttpResponse("This is index page of URL shortner, Currently we are only Accepting api call")


class TinyUrlView(viewsets.ModelViewSet):
    queryset = TinyUrl.objects.all()
    serializer_class = TinyUrlSerializer




