from django.contrib.auth.models import AbstractUser, UserManager as DjangoUserManager
from django.db import models

__all___ = (
    'User',
)


class UserManager(DjangoUserManager):
    def create_django_user(self, username, password, **extra_fields):
        user = User.objects.create_user(
            username=username,
            password=password,
            **extra_fields,
        )
        return user


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

    objects = UserManager()

    def __str__(self):
        return f'{self.pk} {self.username}'
