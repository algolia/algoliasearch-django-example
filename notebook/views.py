from django.shortcuts import render
from django.conf import settings
from django.contrib.algoliasearch import get_adapter
from .models import Contact

def index(request):
    return render(request, 'notebook/index.html')

def auto_complete(request):
    context = {
        'appID': settings.ALGOLIA_APPLICATION_ID,
        'searchKey': settings.ALGOLIA_SEARCH_API_KEY,
        'indexName': get_adapter(Contact).index_name
    }
    return render(request, 'notebook/auto_complete.html', context)

def instant_search(request):
    context = {
        'appID': settings.ALGOLIA_APPLICATION_ID,
        'searchKey': settings.ALGOLIA_SEARCH_API_KEY,
        'indexName': get_adapter(Contact).index_name
    }
    return render(request, 'notebook/instant_search.html', context)
