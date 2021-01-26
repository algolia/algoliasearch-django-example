from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^auto-complete$', views.auto_complete, name='auto_complete'),
    url(r'^instant-search$', views.instant_search, name='instant_search')
]

app_name = 'notebook'