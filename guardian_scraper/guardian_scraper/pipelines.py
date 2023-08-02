from pymongo import MongoClient
from scrapy.exceptions import DropItem
import os 

class MongoDBPipeline(object):

    @classmethod
    def from_crawler(cls, crawler):
        return cls(mongo_conn=crawler.settings.get('MONGODB_CONNECTION'))

    def __init__(self, mongo_conn):
        client = MongoClient(mongo_conn)
        db = client['guardian-data']
        self.collection = db.news

    def process_item(self, item, spider):
        self.collection.insert_one(item)
        return item