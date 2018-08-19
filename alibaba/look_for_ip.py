
def find(ip):
	result = '-1'
	ip_list = ip.split('.')
	ips = {"1.1.1.0/24": 123, "1.1.2.0/28": 345, "1.2.0.0/16": 789}
	for p in (ips.keys()):
		count = 0
		flag = 0
		# print(p.split('.')[:-1])
		for i, j in enumerate(p.split('.')[:-1]):
			if j == ip_list[i]:
				count = count +1
		if count == 3:
			for i in range(int(p.split('.')[-1].split('/')[-1])+1):
				if int(ip_list[-1]) == i:
					flag = 1
		if flag == 1:
			# print(ips[p])
			result = ips[p]
		# else:
		# 	print('-1')
	print(result)


if __name__ == "__main__":
	# ip = input('请输入您的IP(eg:1.1.1.1):')
	# find(ip)
	find('1.1.2.213')