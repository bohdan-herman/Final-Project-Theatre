from django.urls import path
from .views import  CreateReservationView, CreatePlayView, UpdatePlayView, DeletePlayView, PlayView

urlpatterns = [
    path("<int:pk>/reserve", CreateReservationView.as_view(), name = "create_reservation"),
    path('create', CreatePlayView.as_view(), name = "create_play"),
    path('<int:pk>/update', UpdatePlayView.as_view(), name = "update_play"),
    path('<int:pk>/delete', DeletePlayView.as_view(), name = "delete_play"),
    path('<int:pk>/', PlayView.as_view(), name = "play_page"),
]