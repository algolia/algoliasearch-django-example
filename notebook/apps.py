from django.apps import AppConfig
import algoliasearch_django as algoliasearch

from .index import ContactIndex


class NotebookConfig(AppConfig):
    name = 'notebook'

    def ready(self):
        Contact = self.get_model('Contact')
        algoliasearch.register(Contact, ContactIndex)
