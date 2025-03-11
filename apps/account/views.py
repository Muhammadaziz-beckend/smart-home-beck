from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.authtoken.views import ObtainAuthToken

from .serializers import AuthTokenSerializer, RegisterSerializer


class Register(GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):

        serializer = RegisterSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        user = serializer.save()

        token = Token.objects.get_or_create(user=user)[0].key

        return Response(
            {"token": token},
            status=status.HTTP_201_CREATED,
        )
    

class Login(GenericAPIView):
    serializer_class = AuthTokenSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data, context={"request": request}
        )
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        token, created = Token.objects.get_or_create(user=user)
        return Response(
            {
                "token": token.key,
            },
            status=status.HTTP_201_CREATED if created else status.HTTP_200_OK,
        )
    

class Logout(GenericAPIView):

    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        # Проверка для Swagger
        if getattr(self, 'swagger_fake_view', False):
            return Response()

        try:
            request.user.auth_token.delete()
            return Response(
                {"message": "Успешно вышел из системы."}, status=status.HTTP_200_OK
            )
        except Exception as e:
            return Response(
                {"error": "Что-то пошло не так при выходе из системы."},
                status=status.HTTP_400_BAD_REQUEST,
            )