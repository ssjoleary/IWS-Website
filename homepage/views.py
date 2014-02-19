from django.shortcuts import render
from django.views import generic
from django.core.urlresolvers import reverse

# Create your views here.

def index(request):
    template_name = 'homepage/index.html'
    return render(request, template_name)