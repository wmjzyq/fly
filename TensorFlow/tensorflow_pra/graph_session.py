import tensorflow as tf

const1 = tf.constant([[2,2]])
const2 = tf.constant([[4],
					  [4]])

multiple = tf.matmul(const1,const2)
print(multiple)
#创建session会话
sess = tf.Session()

#用session的run方法来实际运行
result = sess.run(multiple)
print(result)

if const1.graph is tf.get_default_graph():
	print('const1所在的图（Graph）是当前上下文默认的图')

#关闭session 方法
sess.close()
#with比较好
with tf.Session() as sess:
	result2 = sess.run(multiple)
	print('multiple的结果是{}'.format(result2))