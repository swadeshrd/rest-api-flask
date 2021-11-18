import codecs
import logging
import os
from configparser import ConfigParser


APP_NAME = ""
BASE_DIR_PATH = os.path.dirname(__file__)
PARENT_DIR_PATH = os.path.abspath(os.path.join(BASE_DIR_PATH, os.pardir))
CONFIG_PATH = os.environ.get(
    os.path.join(BASE_DIR_PATH, "..", "config.conf"), os.path.join(BASE_DIR_PATH, "config.conf")
)

config = ConfigParser()

with codecs.open(CONFIG_PATH) as cf:
    config.read_file(cf)

NODE_IP = config.get("general", "NODE_IP")
ENVIRONMENT = config.get("general", "ENVIRONMENT")
IS_LOCAL = ENVIRONMENT == 'local'

if IS_LOCAL:
    LOG_PATH = os.path.join(BASE_DIR_PATH, "logs", "api")
    LOG_LEVEL = logging.DEBUG
else:
    LOG_PATH = os.path.join(PARENT_DIR_PATH, "logs", "api")
    LOG_LEVEL = logging.INFO

if not os.path.isdir(LOG_PATH):
    os.makedirs(LOG_PATH)

SQLALCHEMY_CONFIG = {
    
    "SQLALCHEMY_DATABASE_URI" : "mysql+pymysql://{user}:{password}@{host}:{port}/{dbname}".format(
        user=config.get("db", "USER"),
        password=config.get("db", "PASSWORD"),
        host=config.get("db", "HOST"),
        port=config.get("db", "PORT"),
        dbname=config.get("db", "NAME"),
    ),
    "SQLALCHEMY_TRACK_MODIFICATIONS" : False,
    "SQLALCHEMY_ECHO" : IS_LOCAL,
}

REDIS_CONFIG = {
    "CACHE_TYPE": "redis",
    "CACHE_REDIS_URL": "redis://{user}:{password}@{server}:{port}/0".format(
        user=config.get("redis", "USER"),
        password=config.get("redis", "PASSWORD"),
        server=config.get("redis", "SERVER"),
        port=config.get("redis", "PORT"),
    ),
    "CACHE_DEFAULT_TIMEOUT": config.get("redis", "EXPIRY"),
    "CACHE_KEY_PREFIX": f"{APP_NAME}-{ENVIRONMENT}-",
}

FLASK_CONFIG = {
    "DEBUG": IS_LOCAL,
}

CONFIGS = {**FLASK_CONFIG, **SQLALCHEMY_CONFIG, **REDIS_CONFIG}