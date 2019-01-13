from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import Card

User = get_user_model()

__all__ = (
    'CardSerializer',
)


class CardSerializer(serializers.ModelSerializer):

    class Meta:
        model = Card
        fields = (
            'id',
            'title',
            'description',
            'pos',
            'img_cover',
            'list_id',
            'created_date',
            'modified_date',
        )
