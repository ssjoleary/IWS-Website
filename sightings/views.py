import json
from django.core import serializers
from django.views import generic

from sightings.models import Sighting
from speciesguide.models import Species

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils import simplejson

# Create your views here.


class IndexView(generic.ListView):
    template_name = 'sightings/index.html'
    context_object_name = 'sightings_list'

    def get_queryset(self):
        # Return the last twenty five.
        return Sighting.objects.order_by('pk')[:25]


class DetailView(generic.DetailView):
    model = Sighting
    template_name = 'sightings/detail.html'


def get_sighting(request):
    result = serializers.serialize('json', Sighting.objects.all(), use_natural_keys=True)
    return HttpResponse(result, mimetype='application/json')


@csrf_exempt
def get_specific_sighting(request):
    if request.method == 'POST':
        searchquery = json.loads(request.body)

        if searchquery['county'] == 'Any...' and searchquery['species'] == 'Any...':
            result = serializers.serialize('json', Sighting.objects.all(), use_natural_keys=True)

        elif searchquery['county'] == 'Any...' and searchquery['species'] != 'Any...':
            speciesItem = Species.objects.get(specname__contains=searchquery['species'])
            speciesPK = speciesItem.pk
            result = serializers.serialize('json', Sighting.objects.filter(species__exact=speciesPK)
                , use_natural_keys=True)

        elif searchquery['county'] != 'Any...' and searchquery['species'] == 'Any...':
            result = serializers.serialize('json', Sighting.objects.filter(location__contains=searchquery['county'])
                , use_natural_keys=True)

        elif searchquery['county'] != 'Any...' and searchquery['species'] != 'Any...':
            speciesItem = Species.objects.get(specname__contains=searchquery['species'])
            speciesPK = speciesItem.pk
            result = serializers.serialize('json', Sighting.objects.filter(species__exact=speciesPK
            ).filter(location__contains=searchquery['county']), use_natural_keys=True)

        return HttpResponse(result, mimetype='application/json')


@csrf_exempt
def post_sighting(request):
    if request.method == 'POST':
        searchquery = json.loads(request.body)

        speciesItem = Species.objects.get(specname__contains=searchquery['species'])
        #speciesPK = speciesItem.pk
        sighting = Sighting(sub_date=searchquery['date'], species=speciesItem, animals=searchquery['animals'],
                            location=searchquery['location'], latitude=searchquery['lat'], longitude=searchquery['lng'],
                            name=searchquery['name'])
        sighting.save()

        #data_to_dump = {'success': 'success'}
        #data = simplejson.dumps(data_to_dump)
        #return HttpResponse(data, mimetype='application/json')
        result = serializers.serialize('json', Sighting.objects.all(), use_natural_keys=True)
        return HttpResponse(result, mimetype='application/json')