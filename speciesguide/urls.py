from django.conf.urls import patterns, url

from speciesguide import views

urlpatterns = patterns('',
    # ex: /species/
    url(r'^$', views.IndexView.as_view(), name='index'),
    # ex: /species/5
    url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
    )