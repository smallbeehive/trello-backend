from django.contrib.auth import get_user_model
from django.db import models

from lists.models import List

User = get_user_model()

__all___ = (
    'Card',
)


class Card(models.Model):
    title = models.CharField(
        verbose_name="Card's title",
        max_length=150,
    )
    description = models.TextField(
        verbose_name="Card's description",
        blank=True
    )
    pos = models.DecimalField(
        verbose_name="Card's position data",
        default=65535,
        decimal_places=7,
        max_digits=15,
    )
    list_id = models.ForeignKey(
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

    class Meta:
        ordering = ['pos']

    def __str__(self):
        return f'{self.pk} {self.title}'
