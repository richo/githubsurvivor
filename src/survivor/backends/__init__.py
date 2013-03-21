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

def _backend_name():
    return config.get('backend', 'github')

def backend_for(config):
    "Import and return the backend according to `config`."
    module_name = 'survivor.backends.%s' % _backend_name()
    return __import__(module_name, fromlist=module_name)

def issue_importer():
    return backend_for(config).issue_importer(config)

def web_theme():
    backend_name = _backend_name()
    return {'html_classname': backend_name,
            'appname': '%s SURVIVOR' % backend_name.upper()}
