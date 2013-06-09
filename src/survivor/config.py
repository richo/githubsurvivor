from os.path import join
from derpconf.config import Config as c, verify_config, generate_config

# Core options

c.define('BACKEND',
         'github',
         'Specify issue-tracking backend')

c.define('DB',
         'githubsurvivor',
         'Mongo database to use as local datastore')

c.define('FLASK_DEBUG',
         False,
         'Whether to display the interactive debugger on error. Don\'t enable this in publicly-accessible environments.')

c.define('FLASK_SETTINGS',
         {'host': '127.0.0.1', 'port': 5000},
         'Options to pass to Flask initialiser')

# GitHub options

c.define('GITHUB_REPO',
         '99designs/githubsurvivor',
         'Specify the GitHub repo you want to report on',
         'GitHub')

c.define('GITHUB_OAUTH_TOKEN',
         'secret',
         'OAuth token for accessing your repo. See https://help.github.com/articles/creating-an-oauth-token-for-command-line-use',
         'GitHub')

# JIRA options

c.define('JIRA_SERVER',
         'https://jira.example.com',
         'JIRA server URL',
         'JIRA')

c.define('JIRA_USERNAME',
         'username',
         'Authorised JIRA username',
         'JIRA')

c.define('JIRA_PASSWORD',
         'password',
         'JIRA account password',
         'JIRA')

c.define('JIRA_PROJECT',
         'PROJECT',
         'JIRA project key',
         'JIRA')

# Reporting options

c.define('LEADERBOARD_USERS',
         [],
         'Optional list of users to display in the bug leaderboards. Leave this empty to include all repo contributors.',
         'Reporting')

c.define('REPORTING_WINDOW',
         'month',
         'Size of reporting window; one of week, sprint, month',
         'Reporting')

c.define('REPORTING_SPRINT_START_WEEKDAY',
         'monday',
         'Day of week starting a sprint-based reporting window',
         'Reporting')

c.define('REPORTING_SPRINT_LENGTH_WEEKS',
         2,
         'Length of sprint-based reporting window',
         'Reporting')

c.define('REPORTING_FIRST_SPRINT_WEEK_OF_YEAR',
         1,
         'Week of year in which the first sprint begins',
         'Reporting')

# API

class Config(object):

    def load(self, config_path):
        self._config = c.load(config_path or self.default_path())

    def default_path(self):
        return join(app_root(), 'config.py')

    def __getattr__(self, key):
        if not self._config: raise 'Not initialised'
        return getattr(self._config, key)

def generate():
    generate_config()
