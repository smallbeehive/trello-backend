from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import List

User = get_user_model()

__all__ = (
    'ListSerializer',
)


class ListSerializer(serializers.ModelSerializer):

    class Meta:
        model = List
        fields = (
            'id',
            'title',
            'pos',
            'boardId',
            'created_date',
            'modified_date',
        )
