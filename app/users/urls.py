from django.urls import path

from .apis import (
    UserListCreateAPIView,
    UserLoginAPIView,
    UserLogoutAPIView,
)

urlpatterns = [
    path('', UserListCreateAPIView.as_view()),
    path('login/', UserLoginAPIView.as_view()),
    path('logout/', UserLogoutAPIView.as_view()),
]
