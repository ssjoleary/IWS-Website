import json
from django.core import serializers
from django.views import generic

from sightings.models import Sighting

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

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


@csrf_exempt
def get_specific_sighting(request):
    if request.is_ajax():
        if request.method == 'POST':
            searchquery = json.loads(request.body)
            result = serializers.serialize('json', Sighting.objects.filter(location__contains=searchquery['county']),
                                           use_natural_keys=True)

    return HttpResponse(result, mimetype='application/json')