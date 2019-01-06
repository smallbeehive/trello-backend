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

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return UserSerializer
        else:
            return UserCreateSerializer
