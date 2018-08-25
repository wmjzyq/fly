#-*- coding: UTF-8 -*-
import re
import os
import jieba
import pymysql
from sklearn.externals import joblib

reg = re.compile(r'<[^>]+>',re.S)
tags = {0:'news_entertainment',
		1:'news_finance',
		2:'news_history',
		3:'news_military',
		4:'news_regimen',
		5:'news_society',
		6:'news_sports',
		7:'news_tech',
		8:'news_world',}

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
	file_name = r'E:\python\project\src\classify\stopword.txt'
	stopwords = stopwordslist(file_name)
	outstr = ''
	for word in document:
		if word not in stopwords:
			if word != '\t':
				outstr += word
				outstr += " "
	return outstr

def classify(new):
	new = reg.sub('', new)
	new_list = [word_segmentation(new)]
	vectorizer = joblib.load(r'E:\python\project\src\classify\vector')
	tfidf_model = vectorizer.transform(new_list)
	clf = joblib.load(r'E:\python\project\src\classify\Bayesian.pkl')
	pred = clf.predict(tfidf_model)[0]
	return tags[pred]
