from django.conf.urls import url

from . import views

app_name = 'Polls'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<question_id>\d+)/$', views.details, name='details'),
    url(r'^(?P<question_id>\d+)/results.', views.results, name='results'),
    url(r'^(?P<question_id>\d+)/vote.', views.vote, name='vote'),
]