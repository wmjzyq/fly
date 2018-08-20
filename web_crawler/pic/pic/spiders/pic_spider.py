import scrapy
from lxml import etree
class PicSpider(scrapy.Spider):
	name = 'pic'
	allowed_domains = ['taobao.com']
	start_urls = [
		"https://s.taobao.com/search?q=%E7%AC%94%E8%AE%B0%E6%9C%AC&refpid=430269_1006&source=tbsy&style=grid&tab=all&pvid=41ca1f4c794c16e563c2095fdf1269bb&clk1=b2e4a75d0ba6cd43bc48e7e1a0fe25cd&spm=a21bo.2017.201856-sline.4.5af911d9RT8FgB&cps=yes&ppath=20000%3A21660"
	]

	def parse(self, response):
		# seletor = etree.HTML(response.text)
		# # filename = './test.txt'
		# url = seletor.xpath('//*[@id="mainsrp-itemlist"]/div/div/div[1]/div/img/@data-src')
		# print(url)
		print(response.text)