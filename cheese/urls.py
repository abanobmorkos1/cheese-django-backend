
from django.contrib import admin
from django.urls import path , include
from rest_framework import routers
from cheeseapp.views import cheeseViewSet


router = routers.DefaultRouter()

router.register(r'cheese', cheeseViewSet)

urlpatterns = [
    path('' , include(router.urls)),
    path('admin/', admin.site.urls),
]
