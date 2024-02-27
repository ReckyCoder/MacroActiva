from django.shortcuts import render

from django.views.generic import ListView

# Create your views here.


class MODEL_NAMEListView(ListView):
    # model = MODEL_NAME
    template_name = "TEMPLATE_NAME"

