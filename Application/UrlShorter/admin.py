from django.contrib import admin
from .models import TinyUrl

admin.site.register(TinyUrl)  # registering my database to be visible on admin pannel
