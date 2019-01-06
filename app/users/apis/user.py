from django.contrib.auth import get_user_model
from rest_framework import generics, permissions

from ..serializers import (
    UserSerializer,
    UserCreateSerializer,
)

User = get_user_model()

__all__ = (
    'UserListCreateAPIView',
)


class UserListCreateAPIView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
