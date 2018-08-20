from urllib.request import urlretrieve

import os
import scrapy
from scrapy.http import Request
from lxml import etree
from liji import items

class Myspider(scrapy.Spider):
	name = 'liji'
	allowed_domains = ['lizhi.fm']
	bash_url = 'http://www.lizhi.fm/user/2552360964061657132/p/'
	bashurl = '.html'

	def start_requests(self):
		for i in range(1,102):
			url = self.bash_url + str(i) + self.bashurl
			yield Request(url,self.parse)

	def get_info(self,response):
		item = items.LijiItem()
		seletor = etree.HTML(response.text)
		fm_name = seletor.xpath('/html/body/div[1]/div[2]/div[3]/div[1]/div/div[2]/h1/text()')
		fm_time = seletor.xpath('/html/body/div[1]/div[2]/div[3]/div[1]/div/div[2]/p[1]/span[1]/text()')
		fm_long = seletor.xpath('/html/body/div[1]/div[2]/div[3]/div[1]/div/div[2]/p[1]/span[2]/text()')
		fm_author = seletor.xpath('/html/body/div[1]/div[2]/div[3]/div[1]/div/div[2]/p[2]/span/a/text()')
		fm_id = response.url[-19:]
		item['fm_name'] = fm_name[0]
		item['fm_time'] = fm_time[0]
		item['fm_long'] = fm_long[0]
		item['fm_author'] = fm_author[0]
		item['fm_id'] = fm_id
		fm_time_new = str(fm_time[0]).replace('-','/')
		url = 'http://cdn5.lizhi.fm/audio/'+fm_time_new+'/'+fm_id+'_ud.mp3'
		print(url)
		self.fm_download(url,fm_author[0],fm_name[0])
		return item

	def fm_download(self,url,author,fm_name):
		file_path = author
		if not os.path.exists(file_path):
			os.makedirs(file_path)
		file_path = os.path.join(file_path,fm_name)+'.mp3'
		print(file_path)
		urlretrieve(url,file_path)

	def parse(self, response):
		seletor = etree.HTML(response.text)
		urls = seletor.xpath('/html/body/div[1]/div[2]/div[4]/ul/li/a/@href')
		for url in urls:
			url = 'http://www.lizhi.fm'+url
			yield Request(url,self.get_info)
			print(url)