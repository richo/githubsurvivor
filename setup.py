from os.path import dirname, join
from setuptools import setup

def slurp(fname):
    path = join(dirname(__file__), fname)
    with open(path) as f:
        f.read()

setup(
    name='GitHub Survivor',
    version='0.0.1',
    author='99designs',
    author_email='stuart.campbell@99designs.com',
    description='A retro-style bug leaderboard',
    license='MIT',
    keywords='bug dashboard leaderboard github jira',
    url='https://github.com/99designs/githubsurvivor',
    packages=('survivor',
              'survivor.backends',
              'survivor.models',
              'survivor.tasks',
              'survivor.web'),
    package_dir={'': 'src'},
    long_description=slurp('README.md'),
    classifiers=('Development Status :: 4 - Beta',),
    entry_points={
        'console_scripts': [
            'githubsurvivor=survivor.web:main',
            'githubsurvivor-sync=survivor.tasks.sync:main',
        ],
    },
)
