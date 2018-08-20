# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
from liji import settings


class LijiPipeline(object):
	def __init__(self):
		self.client = pymongo.MongoClient(host=settings.MOGO_HOST, port=settings.MOGO_PORT)
		self.db = self.client[settings.MOGO_DB]
		self.table = self.db[settings.MOGO_TABLE]

	def process_item(self, item, spider):
		postItem = dict(item)
		self.table.insert(postItem)
		return item
