from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from settings import APP_NAME, CONFIGS

app = Flask(APP_NAME)
app.config.from_mapping(CONFIGS)
db = SQLAlchemy(app)
ma = Marshmallow(app)