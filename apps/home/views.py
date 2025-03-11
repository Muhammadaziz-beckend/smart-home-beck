from django_filters.rest_framework.backends import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import *

from .serializers import *
from utils.mixins import UltraModelMixin
from .models import *


class RoomModelMixin(UltraModelMixin):
    queryset = Room.objects.all()
    lookup_field = "id"
    filter_backends = [
        SearchFilter,
        DjangoFilterBackend,
        OrderingFilter,
    ]
    search_fields = ["name"]
    ordering = ["id"]
    serializer_classes = {
        "list": ListRoomSerializer,
        "retrieve": RetrieveRoomSerializer,
        "create": CreateRoomSerializer,
        "update": CreateRoomSerializer,
    }
    permission_classes_by_active = {
        "list": [IsAuthenticated],
        "retrieve": [IsAuthenticated],
        "create": [IsAuthenticated],
        "update": [IsAuthenticated | IsAdminUser],
    }
