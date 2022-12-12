import os
from decouple import config

class Config(object):

    basedir = os.path.abspath(os.path.dirname(__file__))

    # Set up the App SECRET_KEY
    SECRET_KEY = config('SECRET_KEY', default='S#perS3crEt_007')

    # Read a connection file, ex:(mysql://user:password@127.0.0.1:3306/bd_name)
    with open('db_connection.txt', encoding='utf8') as f:
        for line in f:
            SQLALCHEMY_DATABASE_URI = line
    
    print(SQLALCHEMY_DATABASE_URI)
    # This will create a file in <app> FOLDER
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'db.sqlite3')
    # mysql://user:password@127.0.0.1:3306/bd_name
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProductionConfig(Config):
    DEBUG = False

    # Security
    SESSION_COOKIE_HTTPONLY = True
    REMEMBER_COOKIE_HTTPONLY = True
    REMEMBER_COOKIE_DURATION = 3600

    # PostgreSQL database
    SQLALCHEMY_DATABASE_URI = '{}://{}:{}@{}:{}/{}'.format(
        config('DB_ENGINE', default='postgresql'),
        config('DB_USERNAME', default='appseed'),
        config('DB_PASS', default='pass'),
        config('DB_HOST', default='localhost'),
        config('DB_PORT', default=5432),
        config('DB_NAME', default='appseed-flask')
    )


class DebugConfig(Config):
    DEBUG = True


# Load all possible configurations
config_dict = {
    'Production': ProductionConfig,
    'Debug': DebugConfig
}
