import tensorflow as tf
import numpy_pra as np
import pandas as pd

'''
构建图、创建会话
'''
# matrix1 = tf.constant([[3.,3.]])
# matrix2 = tf.constant([[2.],[2.]])
# product = tf.matmul(matrix1,matrix2)
#
# with tf.Session() as sess:
# 	result = sess.run([product])
# 	print(result)
'''
placeholder
'''
# input1 = tf.placeholder(tf.float32)
# input2 = tf.placeholder(tf.float32)
# output = tf.multiply(input1, input2)
# with tf.Session() as sess:
# 	print(sess.run([output], feed_dict={input1:[7.], input2:[2.]}))

# with tf.variable_scope("foo") as scope:
# 	v = tf.get_variable("v", [1])
# with tf.variable_scope("foo", reuse=True):
# 	v1 = tf.get_variable("v", [1])
# assert v1 == v

'''
name_scope
1.hello/
2.arr1:0
3.scope_name:
'''
# with tf.name_scope('hello') as name_scope:
# 	arr1 = tf.get_variable("arr1",shape=[2,10],dtype=tf.float32)
# 	print(name_scope)
# 	print(arr1.name)
# 	print('scope_name:{}'.format(tf.get_variable_scope().original_name_scope))

'''
variable_scope
<tensorflow.python.ops.variable_scope.VariableScope object at 0x000001D097E69C18>
hello
hello/arr1:0
hello/
hello/xixi/
hello/xixi
'''
# with tf.variable_scope('hello') as variable_scope:
# 	arr1 = tf.get_variable('arr1',shape=[2,10],dtype=tf.float32)
# 	print(variable_scope)
# 	print(variable_scope.name)
# 	print(arr1.name)
# 	print(tf.get_variable_scope().original_name_scope)
#
# 	with tf.variable_scope('xixi') as v_scope2:
# 		print(tf.get_variable_scope().original_name_scope)
# 		print(v_scope2.name)

'''

'''
# with tf.name_scope('name1'):
# 	with tf.variable_scope('var1'):
# 		w = tf.get_variable('w',shape=[2])
# 		res = tf.add(w,[3])

"""
获取变量作用域
"""
# with tf.variable_scope('foo') as foo_scope:
# 	v = tf.get_variable('v',[1])
# with tf.variable_scope(foo_scope):
# 	w = tf.get_variable('w',[1])
# 	print(foo_scope.name)

'''
2
'''
# with tf.variable_scope('foo') as foo_scope:
# 	assert foo_scope.name == "foo"
# with tf.variable_scope('bar'):
# 	with tf.variable_scope('baz') as other_scope:
# 		assert other_scope.name == 'bar/baz'
# 		with tf.variable_scope(foo_scope) as foo_scope2:
# 			assert foo_scope2.name == 'foo'

# with tf.variable_scope('foo',initializer=tf.constant_initializer(0.4)):
# 	v = tf.get_variable('v',[1])
# 	assert v.eval() == 0.4
# 	w = tf.get_variable('w',[1],initializer=tf.constant_initializer(0.3))
# 	assert w.eval() == 0.3
# 	with tf.variable_scope('bar'):
# 		a = tf.get_variable('v',[1])
# 		assert v.eval() == 0.4
# 	with tf.variable_scope('baz',initializer=tf.constant_initializer(0.2)):
# 		b = tf.get_variable('v',[1])
# 		assert v.eval() == 0.2

# with tf.variable_scope('foo'):
# 	x = 1.0 + tf.get_variable('v',[1])
# 	assert x.op.name == 'foo/add'

# with tf.variable_scope('foo'):
# 	with tf.name_scope('bar'):
# 		v = tf.get_variable('v',[1])
# 		b = tf.Variable(tf.zeros[1], name='b')
# 		x = 1.0 + v
# assert v.name == 'foo/v:0'
# assert b.name == 'foo/bar/b:0'
# assert x.op.name == 'foo/bar/add'

# with tf.variable_scope("one"):
# 	a = tf.get_variable("v", [1])  # a.name == "one/v:0"
#
# with tf.Session() as sess:
# 	sess.run(tf.initialize_all_variables())
# 	print(sess.run(a))

# fc_mean,fc_var = tf.nn.moments(Wx_plus_b,axes=[0],)
# scale = tf.Variable(tf.ones([out_size]))
# shift = tf.Variable(tf.zeros(out_size))
# epsilon = 0.001
# Wx_plus_b = ()

'''
一个网上的例子
'''
# def add_layer(inputs, in_size, out_size, activation_function=None):
#     # add one more layer and return the output of this layer
#     Weights = tf.Variable(tf.random_normal([in_size, out_size]))
#     biases = tf.Variable(tf.zeros([1, out_size]) + 0.1)
#     Wx_plus_b = tf.matmul(inputs, Weights) + biases
#     if activation_function is None:
#         outputs = Wx_plus_b
#     else:
#         outputs = activation_function(Wx_plus_b)
#     return outputs
# # 1.训练的数据
# # Make up some real data
# x_data = np.linspace(-1,1,300)[:, np.newaxis]
# noise = np.random.normal(0, 0.05, x_data.shape)
# y_data = np.square(x_data) - 0.5 + noise
#
# # 2.定义节点准备接收数据
# # define placeholder for inputs to network
# xs = tf.placeholder(tf.float32, [None, 1])
# ys = tf.placeholder(tf.float32, [None, 1])
#
# # 3.定义神经层：隐藏层和预测层
# # add hidden layer 输入值是 xs，在隐藏层有 10 个神经元
# l1 = add_layer(xs, 1, 10, activation_function=tf.nn.relu)
# # add output layer 输入值是隐藏层 l1，在预测层输出 1 个结果
# prediction = add_layer(l1, 10, 1, activation_function=None)
#
# # 4.定义 loss 表达式
# # the error between prediciton and real data
# loss = tf.reduce_mean(tf.reduce_sum(tf.square(ys - prediction),
#                      reduction_indices=[1]))
#
# # 5.选择 optimizer 使 loss 达到最小
# # 这一行定义了用什么方式去减少 loss，学习率是 0.1
# train_step = tf.train.GradientDescentOptimizer(0.1).minimize(loss)
#
#
# # important step 对所有变量进行初始化
# init = tf.initialize_all_variables()
# sess = tf.Session()
# # 上面定义的都没有运算，直到 sess.run 才会开始运算
# sess.run(init)
#
# # 迭代 1000 次学习，sess.run optimizer
# for i in range(1000):
#     # training train_step 和 loss 都是由 placeholder 定义的运算，所以这里要用 feed 传入参数
#     sess.run(train_step, feed_dict={xs: x_data, ys: y_data})
#     if i % 50 == 0:
#         # to see the step improvement
#         print(sess.run(loss, feed_dict={xs: x_data, ys: y_data}))

# a = tf.constant([[1.0, 2.0], [1.0, 2.0], [1.0, 2.0]])
# sess = tf.Session()
# print (sess.run(tf.sigmoid(a)))


# a = tf.constant([-1.0, 2.0])
# with tf.Session() as sess:
# 	b = tf.nn.relu(a)
# 	print (sess.run(b))
'''
dropout
'''
# a = tf.constant([[-1.0, 2.0, 3.0, 4.0]])
# with tf.Session() as sess:
# 	b = tf.nn.dropout(a, 0.5, noise_shape = [1,4])
# 	print (sess.run(b))
# 	b = tf.nn.dropout(a, 0.5, noise_shape = [1,1])
# 	print (sess.run(b))

'''
卷积函数
'''

# input_data = tf.Variable( np.random.rand(10,9,9,3), dtype = np.float32 )
# filter_data = tf.Variable( np.random.rand(2, 2, 3, 2), dtype = np.float32)
# y = tf.nn.conv2d(input_data, filter_data, strides = [1, 1, 1, 1], padding = 'SAME')
# print(y)
a = np.random.rand(10,6,6,3)
b = np.random.rand(2, 2, 3, 10)
print(b)
input_data = tf.Variable( np.random.rand(10,6,6,3), dtype = np.float32 )
filter_data = tf.Variable( np.random.rand(2, 2, 3, 10), dtype = np.float32)
y = tf.nn.conv2d(input_data, filter_data, strides = [1, 1, 1, 1], padding = 'SAME')
output = tf.nn.avg_pool(value = y, ksize = [1, 2, 2, 1], strides = [1, 1, 1, 1],
padding ='SAME')