import os

class Config(object):
    """Base Config Object"""
    DEBUG = False
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'Som3$ec5etK*y'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or ' postgresql://wufgjdiiskncdh:0a8fc13ffbf4ad3c2750afd6898483e0566236f80be8788edff6c8e2722afd29@ec2-52-7-115-250.compute-1.amazonaws.com:5432/dcki1o7k0rr446'
    SQLALCHEMY_TRACK_MODIFICATIONS = False # This is just here to suppress a warning from SQLAlchemy as it will soon be removed
    UPLOAD_FOLDER = './app/static/img'
    #set DATABASE_URL=postgresql://project1:project1@localhost/project1

class DevelopmentConfig(Config):
    """Development Config that extends the Base Config Object"""
    DEVELOPMENT = True
    DEBUG = True

class ProductionConfig(Config):
    """Production Config that extends the Base Config Object"""
    DEBUG = False