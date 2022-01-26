from abc import ABCMeta
from datetime import datetime
from pymongo import MongoClient
from config import config

class Model(metaclass=ABCMeta):
    def __init__(self, client:MongoClient, db_name=config.MONGODB_NAME):
        print("baseModel self.__class__.__name__ = ", self.__class__.__name__)
        self.col = client[db_name][self.__class__.__name__]
        
    VERSION = 1

    @property
    def index(self) ->list:
        '''GET Index List'''
        return []
    
    @property
    def schema(self) -> dict:
        """Get default document format"""
        return {
            'created_at': datetime.now(),
            'updated_at': datetime.now(),
            '__version__': self.VERSION,
        }

    # 인덱스 생성
    def create_index(self) -> None:
        """Create indexes"""
        if self.index:
            self.col.create_indexes(self.index)

    # default 데이터와 document를 합치는 기능
    def schemize(self, document: dict) -> dict:
        """Generate JSON scheme"""
        return {**self.schema, **document}