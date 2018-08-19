# coding=utf-8
"""
测试对一篇新闻的分类情况
"""

import jieba
import os

tags = [
    #1 社会
    'news_society',
    #2 娱乐
    'news_entertainment',
    #3 军事
    'news_military',
    #4 科技
    'news_tech',
    #5 体育
    'news_sports',
    #6 财经
    'news_finance',
    #7 国际
    'news_world',
    #8 历史
    'news_history',
    #9 养生
    'news_regimen'
]

# 分类词的总数
map_count = {
    "news_society": 0,
    "news_entertainment": 0,
    "news_military": 0,
    "news_tech": 0,
    "news_sports": 0,
    "news_finance": 0,
    "news_world": 0,
    "news_history": 0,
    "news_regimen": 0
}

# 存储词频
map_word = {
    "news_society": {},
    "news_entertainment": {},
    "news_military": {},
    "news_tech": {},
    "news_sports": {},
    "news_finance": {},
    "news_world": {},
    "news_history": {},
    "news_regimen": {}
}

for tag in tags:
    file = open(os.path.dirname(__file__) + '/word_frequency/'+tag+'_frequency.txt')
    lines = file.readlines(3200)
    file.close()
    map = map_word[tag]
    for line in lines:
        line = line.strip('\n')
        split = line.split(' ')
        if len(split) != 2: continue
        word = split[0]
        count = split[1]
        map[word] = count
        map_count[tag] += int(count)

# 读入停用词
file = open(os.path.dirname(__file__) + '/stop_word.dat', encoding='utf-8')
lines = file.readlines()
file.close()
stop_word = set(line.strip('\n') for line in lines)

# 分类
def classify(news):
    # 分词
    seg_list = jieba.cut(news)
    list = set(seg_list)
    seg_list.close()

    map_score = {}

    for tag in tags:
        score = 1.0
        map = map_word[tag]
        for word in list:
            if word not in stop_word and len(word) > 1:
                score += float(map.get(word, 0))/map_count[tag]
        map_score[tag] = score

    # 寻找最大score和其对应的tag
    max_value = -9999
    max_tag = ''
    for tag, value in map_score.items():
        if value > max_value:
            max_value = value
            max_tag = tag

    return max_tag