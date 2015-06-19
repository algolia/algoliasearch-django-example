from django.apps import AppConfig
#import django.contrib.algoliasearch as AlgoliaSearch
from django.contrib import algoliasearch

from .index import ContactIndex


class NotebookConfig(AppConfig):
    name = 'notebook'

    def ready(self):
        Contact = self.get_model('Contact')
        algoliasearch.register(Contact, ContactIndex)
