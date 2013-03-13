"""
This package contains backends for different issue tracking APIs.

Implementations provide a way to import users and issues into the local
database. The importer looks like this:

    class Importer:
        def __init__(self, config)
        def import_users(self)
        def import_issues(self)
"""

from survivor import config

def backend_for(config):
    "Import and return the backend according to `config`."
    module_name = 'survivor.backends.%s' % config.get('backend', 'github')
    return __import__(module_name, fromlist=module_name)

def configured_backend():
    "Import and return the backend specified by the global config."
    return backend_for(config)
