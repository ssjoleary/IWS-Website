from django.shortcuts import render
from django.views import generic
from django.core.urlresolvers import reverse

from sightings.models import Sighting

from django.utils import simplejson
from django.http import HttpResponse

# Create your views here.

class IndexView(generic.ListView):
    template_name = 'sightings/index.html'
    context_object_name = 'sightings_list'

    def get_queryset(self):
        # Return the last five.
        return Sighting.objects.order_by('sub_date')[:25]

class DetailView(generic.DetailView):
    model = Sighting
    template_name = 'sightings/detail.html'

def get_sighting(request):
    result = []

    result.append({"User":"Sam O'Leary"})
    result.append({"Occupation":"Student"})

    return HttpResponse(simplejson.dumps(result), mimetype='text/plain')