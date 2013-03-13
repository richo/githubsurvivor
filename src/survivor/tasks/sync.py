"""
Synchronises local database with the remote issue tracker.
"""

import argparse

from survivor import config
from survivor.backends import backend_for
from survivor.models import User, Issue

def importer_for(config):
    backend = backend_for(config)
    return backend.Importer(config)

def sync(types, verbose=False):

    importer = importer_for(config)

    if 'users' in types:
        if verbose: print 'Synchronising users...'
        User.drop_collection()
        importer.import_users(verbose)

    if 'issues' in types:
        if verbose: print 'Synchronising issues...'
        Issue.drop_collection()
        importer.import_issues(verbose)

if __name__ == '__main__':
    argparser = argparse.ArgumentParser(description='Synchronises local DB with GitHub')
    argparser.add_argument('-v', '--verbose', dest='verbose', action='store_true', help='verbose output')
    argparser.add_argument('types', nargs='*', help='model types to sync')

    args = argparser.parse_args()
    types = args.types or ('users', 'issues')

    sync(types, args.verbose)
