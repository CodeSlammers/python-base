from .config import Config


class DevConfig(Config):
    """Development specific configuration."""
    DEBUG = True

    SQLALCHEMY_DATABASE_URI = "mysql://root@localhost/pythonbase"
