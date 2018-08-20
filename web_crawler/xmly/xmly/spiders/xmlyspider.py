import os
import re
import json
import scrapy

from lxml import etree
from scrapy.http import Request
from json import JSONDecodeError
from urllib.request import urlretrieve
from xmly import items

class Myspider(scrapy.Spider):
	name = 'xmly'
	allowed_domains = ['ximalaya.com']
	bash_url = 'http://www.ximalaya.com/zhubo/p'
	bashurl = '/'

	def start_requests(self):
		for i in range(1,51):
			url = self.bash_url + str(i) + self.bashurl
			yield Request(url,self.parse)

	def get_info(self,response):
		seletor = etree.HTML(response.text)
		fm_author = seletor.xpath('//*[@id="mainbox"]/div/div/div[1]/div[2]/h1/span/text()')
		print(fm_author[0])
		song_ids = seletor.xpath('//*[@id="index_sounds_wrap"]/div/div/@url')
		song_pages = seletor.xpath('//*[@id="index_sounds_wrap"]/div/div/a')
		if song_ids == []:
			song_ids = seletor.xpath('//*[@id="index_sounds_wrap"]/ul/@sound_ids')
			print('11111111111111111111',song_ids)
			for url_id in song_ids:
				fm_url = 'http://www.ximalaya.com/tracks/'+url_id+'.json'
				print(fm_url)
				yield Request(fm_url,self.fm_json,meta={'fm_author':fm_author})
		# print('0000000000', song_ids)
		elif song_pages != []:
			for page in range(1,int(song_pages[-2].text)+1):
				json_url = 'http://www.ximalaya.com'+song_ids[0]+'?page='+str(page)
				print(json_url)
				yield Request(json_url,self.songs_json,meta={'fm_author':fm_author})

	def songs_json(self,response):
		try:
			content = json.loads(response.text)
			html = content.get('html')
			patt = r'sound_ids="(.*?)">'
			song_url_ids = re.compile(patt).findall(html)[0].split(',')
			if song_url_ids != ['']:
				print('song_url_id:', song_url_ids)
				for song_url_id in song_url_ids:
					fm_url = 'http://www.ximalaya.com/tracks/'+str(song_url_id)+'.json'
					print(fm_url)
					yield Request(fm_url,self.fm_json)
		except JSONDecodeError:
			pass

	def fm_json(self,response):
		try:
			content = json.loads(response.text)
			nickname = content.get('nickname')
			# print(nickname)
			album_title = content.get('album_title')
			# print(album_title)
			fm_title = content.get('title')
			# print(fm_title)
			fm_url = content.get('play_path_64')
			# print(fm_url)
			self.fm_dowload(fm_url,str(nickname),str(album_title),str(fm_title))
		except JSONDecodeError:
			pass

	def fm_dowload(self,fm_url,nickname,album_title,fm_title):
		file_path = os.path.join('fm',nickname,album_title)
		print('\n\n\n\n\n\n',file_path)
		if not os.path.exists(file_path):
			os.makedirs(file_path)
		urlretrieve(fm_url,file_path+'/'+fm_title+'.m4a')

	def parse(self, response):
		seletor = etree.HTML(response.text)
		urls = seletor.xpath('//*[@id="explore_user_detail_entry"]/div[1]/div[2]/div/div/div/div[2]/a/@href')
		for url in urls:
			yield Request(url,self.get_info)