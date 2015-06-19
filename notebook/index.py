from django.contrib.algoliasearch import AlgoliaIndex


class ContactIndex(AlgoliaIndex):
    fields = ('name', 'email', 'company', 'address', 'city', 'county',
            'state', 'zip_code', 'phone', 'fax', 'web', 'followers')

    settings = {
        'attributesToIndex': ['name', 'email', 'company', 'city', 'county',
            'unordered(address)', 'state', 'zip_code', 'phone', 'fax',
            'unordered(web)'],
        'attributesForFaceting': ['city', 'company'],
        'customRanking': ['desc(followers)'],
        'queryType': 'prefixAll'
    }
