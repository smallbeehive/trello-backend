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
            'image',
            'list_id',
            'created_date',
            'modified_date',
        )

    # def update(self, instance, validated_data):
    #     validated_data.pop('image', None)
    #     request = self.context.get('request')
    #     card = super().update(instance, validated_data)
    #
    #     if request.FILES:
    #         card.image.save(request.FILES['image'].name, request.FILES['image'])
    #     return card
