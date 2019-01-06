from django.contrib.auth.models import AbstractUser
from django.db import models

__all___ = (
    'User',
)


class User(AbstractUser):
    username = models.EmailField(unique=True)
    nickname = models.CharField(max_length=50, blank=True)
    created_date = models.DateField(
        verbose_name='Created date',
        auto_now_add=True,
    )
    modified_date = models.DateField(
        verbose_name='Modified date',
        auto_now=True,
    )

    def __str__(self):
        return f'{self.pk} {self.username}'
