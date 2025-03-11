from rest_framework import serializers

from .models import *


class ListRoomSerializer(serializers.ModelSerializer):

    class Meta:
        model = Room
        fields = (
            "id",
            "name",
        )


class RetrieveRoomSerializer(serializers.ModelSerializer):

    class Meta:
        model = Room
        fields = "__all__"


class CreateRoomSerializer(serializers.ModelSerializer):

    class Meta:
        model = Room
        fields = ("name",)
