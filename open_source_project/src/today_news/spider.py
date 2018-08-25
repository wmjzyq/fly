import pymysql
import requests
import re
import time
from lxml import etree
from selenium import webdriver


"""
利用模拟浏览器技术自动滚动，获得js渲染之后的页面内容
"""
def auto_roll(url):
	fireFoxOptions = webdriver.FirefoxOptions()
	fireFoxOptions.add_argument('-headless')
	driver = webdriver.Firefox(options=fireFoxOptions)
	try:
		driver.get(url)
		driver.refresh()
		time.sleep(1)
		for i in range(0,3000,100):
			print('Crawling.....please wait')
			time.sleep(1)
			driver.execute_script("window.scrollBy(0,"+str(i)+")")
			driver.execute_script("document.body.scrollTop =0")
		time.sleep(2)
		return driver.page_source
	except:
		print("connect error")
	finally:
		driver.close()


"""
获得最原始的新闻地址，无过滤
"""
def news_url(page_suorce):
	seletor = etree.HTML(page_suorce)
	source_urls = seletor.xpath('/html/body/div/div[4]/div[2]/div[2]/div/div/div/ul/li/div/div[1]/div/div[1]/a/@href')
	return source_urls


"""
过滤源地址中夹杂的其它垃圾地址。比如：广告。
"""
def filter(source_urls):
	patt = "'(http.*?)'"
	a = re.findall(patt,str(source_urls))
	for a in a:
		source_urls.remove(a)
	return source_urls             #过滤之后的地址


"""
获得最终可以点开的新闻真实地址
"""
def real_url(new_source_urls):
	real_urls = []
	for index in range(len(new_source_urls)):
		real_urls.append('https://www.toutiao.com/a'+new_source_urls[index][7:])
	print("real urls----------------------------------------------------------------------")
	print(real_urls)
	return real_urls


"""
爬取title、abstract、media_name、img_url、img_list、article_url、tag
"""
def crawl_new(urls,tag):
	connection = pymysql.connect(host='localhost',
								 port=3306,
								 user='root',
								 password='123456',
								 db='graduate',
								 charset='utf8',
								 cursorclass=pymysql.cursors.DictCursor)

	cursor = connection.cursor()
	for url in urls:
		headers = {
			'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.170 Safari/537.36'
		}
		try:
			response = requests.get(url=url,headers=headers).text
		except:
			continue
		selector = etree.HTML(response)
		article_body = selector.xpath('/html/body/script[4]/text()')
		if article_body != [] and article_body[0].find('tac') == -1:

			re_content = article_body[0].strip('var BASE_DATA = ')
			pattn_title = "title: '([\s\S]*?)',"
			pattn_content = "content: '([\s\S]*?)',"
			pattn_source = "source: '([\s\S]*?)',"
			pattn_time = "time: '([\s\S]*?)'"
			pattn_img = '<img src="([\s\S]*?)" '
			title = re.findall(pattn_title,re_content)[0]
			if re.findall(pattn_content,re_content) != []:
				content = re.findall(pattn_content,re_content)[0].replace('&lt;','<').replace('&gt;','>').replace('&#x3D;','=').replace('&quot;','"')
			else:
				continue
			detail_source = re.findall(pattn_source,re_content)[0]
			time = re.findall(pattn_time,re_content)[0]
			if re.findall(pattn_img,content) != []:
				img_url = re.findall(pattn_img,content)[0]
			else:
				img_url = 'https://s3.pstatp.com/toutiao/resource/ntoutiao_web/static/image/logo_201f80d.png'
			print("标题：",title)
			print("内容：",content)
			print("来源：",detail_source)
			print("时间：",time)
			print("类别：",tag)
			print("图片索引:",img_url)
			print('------------------------------------------------------------------------')
			cursor.execute('insert into article(title, content, detail_source, img_url, tag, time)'
						   ' values(%s, %s, %s, %s, %s, %s)',
						   (title, content, detail_source,img_url, tag, time))
			connection.commit()
		else:
			pass
	cursor.close()
	connection.close()

def run():
	tags = [
		# 1 社会
		'news_society',

		# 2 娱乐
		'news_entertainment',

		# 3 军事
		'news_military',

		# 4 科技
		'news_tech',

		# 5 体育
		'news_sports',

		# 6 财经
		'news_finance',

		# 7 国际
		'news_world',

		# 8 历史
		'news_history',

		# 10 养生
		'news_regimen'
	]
	# tag = 'news_tech'
	base = 'https://www.toutiao.com/ch/'
	for tag in tags:
		url = base + tag + '/'
		print("正在爬取：------------", url)
		page_source = auto_roll(url)
		source_urls = news_url(page_source)
		new_source_urls = filter(source_urls)
		real_urls = real_url(new_source_urls)
		crawl_new(real_urls, tag)

if __name__ == '__main__':
	run()