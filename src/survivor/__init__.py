from os.path import dirname, join, realpath

import mongoengine

def app_root():
    return dirname(dirname(dirname(realpath(__file__))))

def default_config_path():
    return join(app_root(), 'config.py')

def parse_config(path):
    env = {'config': None}
    execfile(path, env)
    return env['config']

def init_db(db_name):
    conn = mongoengine.connect(db_name, tz_aware=True)
    return conn[db_name]

# Global configuration
config = {}

# Database connection
db = None

def init(config_path=None):
    global db
    config.clear()
    config.update(parse_config(config_path or default_config_path()))
    db = init_db(config['db'])
