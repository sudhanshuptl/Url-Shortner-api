from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework import viewsets
from .models import TinyUrl
from .Serializers import TinyUrlSerializer
from django.shortcuts import get_object_or_404
from .logics import base_converter_to_base10


def index(request):
    return HttpResponse("This is index page of URL shortner, Currently we are only Accepting api call")


class TinyUrlView(viewsets.ModelViewSet):
    queryset = TinyUrl.objects.all()
    serializer_class = TinyUrlSerializer


def i_want_to_go_to_my_url(requests, my_tiny_url=None):
    if my_tiny_url:
        get_db_index = base_converter_to_base10(my_tiny_url)
    else:
        get_db_index = None

    get_my_url = get_object_or_404(TinyUrl, my_url=get_db_index)
    context = {
        'myurl': get_my_url.url if 'http' in get_my_url.url else f'https://{get_my_url.url}'
    }
    return render(requests, 'redirect.html', context)


