from django.conf.urls import patterns, url
from encuestas import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^(?P<poll_id>\d+)/$', views.detail, name='details'),
	url(r'^(?P<poll_id>\d+)/resultados/$', views.resultados, name='resultados'),
	url(r'^(?P<poll_id>\d+)/votos/$', views.votos, name='votos'),
)