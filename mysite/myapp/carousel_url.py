from django.urls import path
from .views import  CreateCarouselView, UpdateCarouselView, DeleteCarouselView

urlpatterns = [
    path("create", CreateCarouselView.as_view(), name = "create_carousel"),
    path('<int:pk>/update', UpdateCarouselView.as_view(), name = "update_carousel"),
    path('<int:pk>/delete', DeleteCarouselView.as_view(), name = "delete_carousel"),
]