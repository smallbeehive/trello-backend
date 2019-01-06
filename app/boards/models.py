from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

__all___ = (
    'Board',
)


class Board(models.Model):
    title = models.CharField(
        max_length=150,
        verbose_name="Board's title",
    )
    bgColor = models.CharField(
        max_length=50,
        verbose_name="Board's background color",
        default='rgb(0, 121, 191)',
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
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
