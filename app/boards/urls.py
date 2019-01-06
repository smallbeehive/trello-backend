from django.urls import path

from .apis import BoardListCreateAPIView, BoardRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('', BoardListCreateAPIView.as_view()),
    path('<int:pk>/', BoardRetrieveUpdateDestroyAPIView.as_view()),
]
