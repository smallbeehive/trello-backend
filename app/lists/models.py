from django.contrib.auth import get_user_model
from django.db import models

from boards.models import Board

User = get_user_model()

__all___ = (
    'List',
)


class List(models.Model):
    title = models.CharField(
        max_length=150,
        verbose_name="List's title",
    )
    pos = models.PositiveIntegerField(
        verbose_name="List's position data",
        blank=True
    )
    boardId = models.ForeignKey(
        Board,
        on_delete=models.CASCADE
    )
    created_date = models.DateField(
        verbose_name='Created date',
        auto_now_add=True,
    )
    modified_date = models.DateField(
        verbose_name='Modified date',
        auto_now=True
    )

    def __str__(self):
        return f'{self.pk} {self.title}'
