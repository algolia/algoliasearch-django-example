from django.apps import AppConfig
import algoliasearch_django as algoliasearch
from core import settings

from .index import ContactIndex


class NotebookConfig(AppConfig):
    name = 'notebook'

    def ready(self):
        Contact = self.get_model('Contact')
        if not settings.TESTING:
            algoliasearch.register(Contact, ContactIndex)