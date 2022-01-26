from pymongo import MongoClient
from config import config

# Collection
from .test import Testdb

def get_cursor(uri=config.MONGODB_URI) -> MongoClient:
    """Get MongoDB Cursor"""
    return MongoClient(uri, connect=False)