from django.contrib.auth import get_user_model
from rest_framework import serializers

from lists.serializers import ListSerializer
from users.serializers import UserSerializer
from .models import Board

User = get_user_model()

__all__ = (
    'BoardSerializer',
)


class BoardSerializer(serializers.ModelSerializer):

    user = UserSerializer(read_only=True)
    lists = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Board
        fields = (
            'id',
            'title',
            'bgColor',
            'user',
            'lists',
            'created_date',
            'modified_date',
        )

    def get_lists(self, board):
        lists = board.list_set.all()
        serializers = ListSerializer(lists, many=True)
        return serializers.data
