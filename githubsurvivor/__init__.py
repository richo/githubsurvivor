import mongoengine
from githubsurvivor.config import Config

def init_db(db_name, host=None):
    conn = mongoengine.connect(db_name, host=host, tz_aware=True)
    return conn[db_name]

# Global configuration
config = Config()

# Database connection
db = None

def init(config_path=None):
    global db
    config.load(config_path)
    db = init_db(config.DB, config.DB_HOST)
