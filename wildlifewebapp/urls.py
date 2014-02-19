from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', include('homepage.urls', namespace='homepage')),
    # url(r'^blog/', include('blog.urls')),

    url(r'^speciesguide/', include('speciesguide.urls', namespace="speciesguide")),
    url(r'^sightings/', include('sightings.urls', namespace="sightings")),
    url(r'^admin/', include(admin.site.urls)),
)