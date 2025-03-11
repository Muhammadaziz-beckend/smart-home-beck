from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .ysge import swagger

router = DefaultRouter()

urlpatterns = [
    #
    path("", include(router.urls)),
]

urlpatterns += swagger
