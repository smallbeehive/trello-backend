from django.urls import path

from .apis import ListListCreateAPIView, ListRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('', ListListCreateAPIView.as_view()),
    path('<int:pk>/', ListRetrieveUpdateDestroyAPIView.as_view()),
]
