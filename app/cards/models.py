from django.contrib.auth import get_user_model
from django.db import models

from lists.models import List

User = get_user_model()

__all___ = (
    'Card',
)


class Card(models.Model):
    title = models.CharField(
        max_length=150,
        verbose_name="Card's title",
    )
    description = models.TextField(
        verbose_name="Card's description",
    )
    pos = models.PositiveIntegerField(
        verbose_name="Card's position data",
        default=65535,
    )
    listId = models.ForeignKey(
        List,
        on_delete=models.CASCADE,
    )
    created_date = models.DateField(
        verbose_name='Created date',
        auto_now_add=True,
    )
    modified_date = models.DateField(
        verbose_name='Modified date',
        auto_now=True,
    )

    def __str__(self):
        return f'{self.pk} {self.title}'
