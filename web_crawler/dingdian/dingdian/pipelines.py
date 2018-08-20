# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
from dingdian import settings

class DingdianPipeline(object):
	def __init__(self):
		self.client = pymongo.MongoClient(host=settings.MONGO_HOST,port=settings.MONGO_PORT)
		self.db = self.client[settings.MONGO_DB]
		self.table = self.db[settings.MONGO_TABLE]
	def process_item(self, item, spider):
		postItem = dict(item)
		self.table.insert(postItem)
		return item
