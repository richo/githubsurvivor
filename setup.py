from os.path import dirname, join
from setuptools import setup

def slurp(fname):
    path = join(dirname(__file__), fname)
    with open(path) as f:
        f.read()

setup(
    name='githubsurvivor',
    version='0.0.1',
    author='99designs',
    author_email='stuart.campbell@99designs.com',
    description='A retro-style bug leaderboard',
    long_description=slurp('README.rst'),
    license='MIT',
    keywords='bug dashboard leaderboard github jira',
    url='https://github.com/99designs/githubsurvivor',
    classifiers=['Development Status :: 4 - Beta'],

    packages=['survivor',
              'survivor.backends',
              'survivor.models',
              'survivor.tasks',
              'survivor.web'],

    package_dir={'survivor': 'survivor'},

    install_requires=['Flask==0.9',
                      'mongoengine==0.8.1',
                      'python-dateutil==2.1',
                      'PyGithub==1.16.0',
                      'iso8601==0.1.4',
                      'jira-python==0.13',
                      'derpconf==0.4.8'],

    entry_points={
        'console_scripts': [
            'githubsurvivor=survivor.web:main',
            'githubsurvivor-sync=survivor.tasks.sync:main',
            'githubsurvivor-generate-config=survivor.config:generate'
        ],
    },
)
