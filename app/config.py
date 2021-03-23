import os
####
class Config(object):
    """Base Config Object"""
    DEBUG = False
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'Som3$ec5etK*y'
   # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 
    SQLALCHEMY_DATABASE_URI="postgresql://project1:project1@localhost/project1"
   # SQLALCHEMY_DATABASE_URI='postgresql://hllebyohjzlfgz:c575c24eb703b56c7b873c04d0fa36e9cf1d9d027ed59bfc0540bcb56c20030c@ec2-3-91-127-228.compute-1.amazonaws.com:5432/dapcgoc2a7vob6'
    SQLALCHEMY_TRACK_MODIFICATIONS = False # This is just here to suppress a warning from SQLAlchemy as it will soon be removed
    UPLOAD_FOLDER = './app/static/img'
    #####3set DATABASE_URL=postgresql://project1:project1@localhost/project1

class DevelopmentConfig(Config):
    """Development Config that extends the Base Config Object"""
    DEVELOPMENT = True
    DEBUG = True


class ProductionConfig(Config):
    """Production Config that extends the Base Config Object"""
    DEBUG = False
