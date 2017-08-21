from algoliasearch_django import AlgoliaIndex


class ContactIndex(AlgoliaIndex):
    fields = ('name', 'email', 'company', 'address', 'city', 'county',
              'state', 'zip_code', 'phone', 'fax', 'web', 'followers', 'account_names', 'account_ids')

    settings = {
        'searchableAttributes': ['name', 'email', 'company', 'city', 'county', 'account_names',
                                 'unordered(address)', 'state', 'zip_code', 'phone', 'fax',
                                 'unordered(web)'],
        'attributesForFaceting': ['city', 'company'],
        'customRanking': ['desc(followers)'],
        'queryType': 'prefixAll',
        'highlightPreTag': '<mark>',
        'highlightPostTag': '</mark>',
        'hitsPerPage': 15
    }
