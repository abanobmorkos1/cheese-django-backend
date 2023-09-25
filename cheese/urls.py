
from django.contrib import admin
from django.urls import path , include
from rest_framework import routers
from cheeseapp.views import CheeseViewset


router = routers.DefaultRouter()

router.register(r'cheese', CheeseViewset)

urlpatterns = [
    path('' , include(router.urls)),
    path('admin/', admin.site.urls),
]
