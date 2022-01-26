from flask import Flask
from model import mongodb
def register_connection_pool(app: Flask):
    app.db = mongodb.get_cursor()