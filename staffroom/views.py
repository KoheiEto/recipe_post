from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView


class StaffroomTemplateView(TemplateView):
    template_name = "staffroom/index.html"