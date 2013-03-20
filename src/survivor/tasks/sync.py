"""
Synchronises local database with the remote issue tracker.
"""

import argparse

from survivor.backends import issue_importer
from survivor.models import User, Issue

def sync(types, verbose=False):

    importer = issue_importer()

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
