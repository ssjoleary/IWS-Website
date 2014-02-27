from django.views import generic
from django.core import serializers
from django.shortcuts import render_to_response

from sightings.models import Sighting

# Create your views here.


class IndexView(generic.ListView):
    template_name = 'gmap/index.html'
    context_object_name = 'sightings_list'

    def get_queryset(self):
    # Return the last twenty five.
        return Sighting.objects.order_by('sub_date')[:25]

