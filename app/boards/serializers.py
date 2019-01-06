from django.contrib.auth import get_user_model
from rest_framework import serializers

from users.serializers import UserSerializer
from .models import Board

User = get_user_model()

__all__ = (
    'BoardSerializer',
)


class BoardSerializer(serializers.ModelSerializer):

    user = UserSerializer(read_only=True)

    class Meta:
        model = Board
        fields = (
            'id',
            'title',
            'bgColor',
            'user',
            'created_date',
            'modified_date',
        )
