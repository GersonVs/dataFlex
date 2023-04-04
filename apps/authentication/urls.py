from django.urls import path
from .views import CustomObtainAuthToken, UserCreateAPIView, UserDetailAPIView

urlpatterns = [
    path('token/', CustomObtainAuthToken.as_view()),

    path('create_user/', UserCreateAPIView.as_view()),
    path('detail_user/', UserDetailAPIView.as_view()),
]
