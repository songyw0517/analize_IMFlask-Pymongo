from datetime import datetime
from .baseModel import Model

class Testdb(Model):
    def insert_userInfo(self, document):
        self.col.insert_one(self.schemize(document))

    def get_document(self):
        doc_list = []
        for i in self.col.find():
            doc_list.append(i)
        return doc_list

    def drop_collection(self):
        self.col.drop()

    def update_userInfo(self, doc):
        self.col.update_one({"id":doc['id']}, {"$set":{"pw" :doc['ch_pw']}}, upsert=True) # db업데이트 하기

    def delete_id(self, id):
        self.col.find_one_and_delete({'id':id})