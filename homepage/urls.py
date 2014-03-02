from django.conf.urls import patterns, url

from homepage import views

urlpatterns = patterns('',
    
    url(r'^$', views.index, name='index'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
    # ex: /species/
    #url(r'^$', views.IndexView.as_view(), name='index'),
    # ex: /species/5
    #url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
)