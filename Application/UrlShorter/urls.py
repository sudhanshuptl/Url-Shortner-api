from django.urls import path, include
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register('myurl', views.TinyUrlView)  # tinyuel is url endpoint

urlpatterns = [
    path('', views.index, name='index'),
    path('api/', include(router.urls))
]

