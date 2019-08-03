from django.shortcuts import render
from django.views.generic import ListView
from .models import Destinations
# Create your views here.

class DestinationsView(ListView):
    model = Destinations
    template_name = 'index.html'
