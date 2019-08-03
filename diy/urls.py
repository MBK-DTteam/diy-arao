from django.urls import path, include
from .views import DestinationsView

urlpatterns = [
    path('', DestinationsView.as_view(), name='home'),
]
