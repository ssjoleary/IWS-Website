import json
from django.core import serializers
from django.views import generic

from sightings.models import Sighting

from django.http import HttpResponse

# Create your views here.


class IndexView(generic.ListView):
    template_name = 'sightings/index.html'
    context_object_name = 'sightings_list'

    def get_queryset(self):
        # Return the last five.
        return Sighting.objects.order_by('pk')[:25]


class DetailView(generic.DetailView):
    model = Sighting
    template_name = 'sightings/detail.html'


def get_sighting(request):
    result = serializers.serialize('json', Sighting.objects.all(), use_natural_keys=True)
    return HttpResponse(result, mimetype='application/json')