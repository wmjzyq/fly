import os
import sys
import datetime
import collections
import argparse
import numpy_pra as np
import tensorflow as tf

data_path = './RNN_data'
# 保存训练所得的模型参数文件的目录
save_path = './save'

# 测试时读取模型参数文件的名称
load_file = "train-checkpoint-69"

parser = argparse.ArgumentParser()
# 数据集的目录
parser.add_argument('--data_path', type=str, default=data_path, help='The path of the data for training and testing')
# 测试时读取模型参数文件的名称
parser.add_argument('--load_file', type=str, default=load_file, help='The path of checkpoint file of model variables saved during training')
args = parser.parse_args()
#如果是Python3版本
Py3 = sys.version_info[0] == 3

#将文件根据语句末分隔符<eos>来分割
def read_words(filename):
	with tf.gfile.GFile(filename,'r') as f:
		if Py3:
			return f.read().replace("\n","<eos>").split()
		else:
			return f.read().decode("utf-8").replace("\n","<eos>").split()


# 构造从单词到唯一整数值的映射
# 后面的其他数的整数值按照它们在数据集里出现的次数多少来排序，出现较多的排前面
# 单词 the 出现频次最多，对应整数值是 0
# <unk> 表示 unknown（未知），第二多，整数值为 1
def build_vocab(filename):
	data = read_words(filename)

	#用Counter统计出单词出现的次数，为了之后按单词出现的次数的多少来排序
	counter = collections.Counter(data)
	count_pairs = sorted(counter.items(),key=lambda x: (-x[1],x[0]))

	words, _= list(zip(*count_pairs))
	# 单词到整数的映射
	word_to_id = dict(zip(words, range(len(words))))
	return word_to_id

#将文件里的单词都替换成独一的整数

def file_to_word_ids(filename, word_to_id):
	data = read_words(filename)
	return [word_to_id[word] for word in data if word in word_to_id]

#加载所有的数据，读取所有的单词，把其转成唯一对应的整数值
def load_data(data_path):
	# 确保包含所有数据集文件的data_path文件夹在所有的Python文件
	# 的同级目录下。当然了，你也可以自定义文件夹名和路径
	if not os.path.exists(data_path):
		raise Exception('包含所有数据的文件的{}文件夹不在此目录下，请添加'.format(data_path))

	#三个数据集的路径
	train_path = os.path.join(data_path,'ptb.train.txt')
	valid_path = os.path.join(data_path,'ptb.valid.txt')
	test_path = os.path.join(data_path,'ptb.test.txt')

	#建立词汇表，将所有单词（word）转为唯一对应的整数值（id）