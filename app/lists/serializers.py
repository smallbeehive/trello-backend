from django.contrib.auth import get_user_model
from rest_framework import serializers

from cards.serializers import CardSerializer
from .models import List

User = get_user_model()

__all__ = (
    'ListSerializer',
)


class ListSerializer(serializers.ModelSerializer):

    cards = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = List
        fields = (
            'id',
            'title',
            'pos',
            'boardId',
            'cards',
            'created_date',
            'modified_date',
        )

    def get_cards(self, list):
        cards = list.card_set.all()
        serializers = CardSerializer(cards, many=True)
        return serializers.data
