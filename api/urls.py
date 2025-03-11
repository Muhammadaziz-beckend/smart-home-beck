from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .ysge import swagger
from apps.home.views import RoomModelMixin
from apps.account.views import *

router = DefaultRouter()
router.register("room", RoomModelMixin)

urlpatterns = [
    # auth
    path("auth/login/",Login.as_view()),
    path("auth/logout/",Logout.as_view()),
    path("auth/register/",Register.as_view()),
    # api
    path("", include(router.urls)),
]

urlpatterns += swagger
