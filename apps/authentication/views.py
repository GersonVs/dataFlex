from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer
from dataFlex.serializers import ErrorSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

class UserCreateAPIView(APIView):

    @swagger_auto_schema(
        operation_summary='Criar Usuário',
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'username': openapi.Schema(type=openapi.TYPE_STRING),
                'password': openapi.Schema(type=openapi.TYPE_STRING),
            },
            required=['username', 'password']
        ),
        responses={
            201: openapi.Response(description='Created', schema=UserSerializer),
            400: openapi.Response(description='Bad Request', schema=ErrorSerializer),
        },
        tags=['authentication'],
    )
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = User.objects.create_user(username=username, password=password)

        return Response({
            'username': user.username,
            'id': user.id,
        }, status=status.HTTP_201_CREATED)

class CustomObtainAuthToken(ObtainAuthToken):

    @swagger_auto_schema(operation_summary='Obter Token do Usuário', tags=['authentication'])
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'username': user.username
        })

class UserDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]  
    
    @swagger_auto_schema(
        tags=["authentication"],
        operation_summary="Detalhes do Usuário",
        responses={
            "200": openapi.Response(
                description="Detalhes do Usuário obtidos com sucesso",
                schema=UserSerializer(),
            ),
            "400": openapi.Response(
                description="Credenciais inválidas",
                schema=ErrorSerializer(),
            ),
        },
    )
    def get(self, request, format=None):
        user = request.user
        serializer = UserSerializer(user)
        return Response(serializer.data)