from django.contrib.auth import get_user_model
from django.db import models

from boards.models import Board

User = get_user_model()

__all___ = (
    'List',
)


class List(models.Model):
    title = models.CharField(
        verbose_name="List's title",
        max_length=150,
    )
    pos = models.DecimalField(
        verbose_name="List's position data",
        default=65535,
        decimal_places=7,
        max_digits=15,
    )
    boardId = models.ForeignKey(
        Board,
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
