from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()

__all__ = (
    'UserSerializer',
)


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'nickname',
        )
