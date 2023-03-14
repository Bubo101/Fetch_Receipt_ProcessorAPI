from django.urls import path
from .views import (process_receipts, get_points)

urlpatterns = [
    path("process", process_receipts),
    path("<int:pk>/points", get_points),
]