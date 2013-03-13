from os.path import dirname, join, realpath

import mongoengine

def app_root():
    return dirname(dirname(dirname(realpath(__file__))))

def parse_config(path=None):
    env = {'config': None}
    execfile(path or join(app_root(), 'config.py'), env)
    return env['config']

def init_db(db_name):
    conn = mongoengine.connect(db_name, tz_aware=True)
    return conn[db_name]

# Global configuration
config = parse_config()

# Database connection
db = init_db(config['db'])
