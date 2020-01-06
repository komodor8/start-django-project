from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

# Create your views here.
class IndexView(generic.TemplateView):
    template_name = 'apptesting/index.html'