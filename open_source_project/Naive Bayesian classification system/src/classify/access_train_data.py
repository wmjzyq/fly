import os
import re
import pymysql
import jieba

reg = re.compile(r'<[^>]+>',re.S)
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

"""
概述：读取停用词
参数：停用词文件路径
"""
def stopwordslist(filepath):
	stopwords = [line.strip() for line in open(filepath, 'r', encoding='utf-8').readlines()]
	return stopwords

"""
概述：分词、去停用词
参数：新闻内容
"""
def word_segmentation(new_content):
	document = jieba.cut(new_content.strip(),cut_all=False)
	stopwords = stopwordslist('./stopword.txt')
	outstr = ''
	for word in document:
		if word not in stopwords:
			if word != '\t':
				outstr += word
				outstr += " "
	return outstr


"""
连接数据库
"""
connection = pymysql.connect(host='localhost',
							 port=3306,
							 user='root',
							 password='123456',
							 db='graduate',
							 charset='utf8',
							 cursorclass=pymysql.cursors.DictCursor)

cursor = connection.cursor()

for tag in tags:
	"""
	分类建立目录，没有则创建。
	"""
	print(tag)
	count = 1
	dir_path = os.path.join(r'G:\news',tag)
	if os.path.exists(dir_path) == False:
		os.makedirs(dir_path)
	cursor.execute("select content from article where tag = '{tag}'".format(tag=tag))
	news = cursor.fetchall()

	for new in news:
		content = new["content"]
		new_content = reg.sub('', content)
		file_name = tag + '_' + str(count) + '.txt'
		file_path = os.path.join(dir_path, file_name)
		count = count + 1
		final_content = word_segmentation(new_content)
		print(final_content)
		with open(file_path, mode='w', encoding='utf-8') as file:
			file.write(final_content)
		print('--------------------------------------------------------------------------')
	connection.commit()

cursor.close()
connection.close()
