#-*- coding: UTF-8 -*-
"""
概述：定义find函数，通过‘.’来切分各段。如果前三段相同,则比较第四段是否在范围内，如果在则输出键值。不在返回-1。
时间复杂度：O(n)
"""
def find(ip):
	result = '-1'
	ip_list = ip.split('.')
	ips = {"1.1.1.0/24": 123, "1.1.2.0/28": 345, "1.2.0.0/16": 789}
	for p in (ips.keys()):
		p_list = p.split('.')
		p_sublist = p_list[-1].split('/')
		if ip_list[:-1] == p_list[:-1]:
			if int(ip_list[-1]) >= int(p_sublist[0]) and int(ip_list[-1]) <= int(p_sublist[1]):
				result = ips[p]
	print(result)


if __name__ == "__main__":
	# ip = input('请输入您的IP(eg:1.1.1.1):')
	# find(ip)
	find('1.1.2.1')