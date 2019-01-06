from django.urls import path

from .apis import (
    UserListCreateAPIView,
)

urlpatterns = [
    path('', UserListCreateAPIView.as_view()),
]
