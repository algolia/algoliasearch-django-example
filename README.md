# AlgoliaSearch Django Example

This is a Django application indexing 500 `Contact` objects and providing auto-completion and instant-search samples. See [algoliasearch-django](https://github.com/algolia/algoliasearch-django) package.

A `Contact` is defined by:

* A name
* An email adress
* A company name

An [Algolia](https://www.algolia.com) account is required to test it.

## Dependencies

```bash
$ pip install algoliasearch-django
```

## Installation

```bash
$ git clone https://github.com/algolia/algoliasearch-django-example
$ cd algoliasearch-django-example
$ python manage.py migrate
$ python manage.py createsuperuser
```

## Configure the credentials

You can add your credentials in `core/settings.py` or you can export them in your environment:

```bash
$ export ALGOLIA_APPLICATION_ID=XXXXX
$ export ALGOLIA_API_KEY=XXXXX
$ export ALGOLIA_SEARCH_ONLY_API_KEY=XXXXX
```

## Populate the DB and start indexing

```bash
$ python manage.py loaddata contacts.json
$ python manage.py algolia_reindex
```

## Start the application

```bash
$ python manage.py runserver
```

Enjoy your `http://localhost:8000` examples!

![Instant-search](instant-search.png)

![Auto-complete](auto-complete.png)
