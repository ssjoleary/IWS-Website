from django.views import generic

from speciesguide.models import Species

# Create your views here.


class IndexView(generic.ListView):
    template_name = 'speciesguide/index.html'
    context_object_name = 'species_list'

    def get_queryset(self):
        # Return the last twenty five.
        return Species.objects.order_by('specname')[:25]


class DetailView(generic.DetailView):
    model = Species
    template_name = 'speciesguide/detail.html'