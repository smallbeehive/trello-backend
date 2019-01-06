from django.urls import path

from boards.apis import BoardListCreateAPIView

urlpatterns = [
    path('', BoardListCreateAPIView.as_view())
]
