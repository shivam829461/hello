from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView

class ServicePageView(TemplateView):
    template_name = 'services.html'

