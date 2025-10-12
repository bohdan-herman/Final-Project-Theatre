from django.urls import path
from .views import  CreateReservationView, PlayView

urlpatterns = [
    path("<int:pk>/reserve", CreateReservationView.as_view(), name = "create_reservation"),
    path('<int:pk>/', PlayView.as_view(), name = "play_page"),
]