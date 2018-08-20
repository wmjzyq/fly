from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets('MNIST_data/', one_hot=True)
import tensorflow as tf
'''
打印mnist中的信息
'''
# print('输入数据:', mnist.train.images)
# print('输入数据的shape:', mnist.train.images.shape)
import pylab
# im = mnist.train.images[5]
# print(im)
# im = im.reshape(-1,28)
# pylab.imshow(im)
# pylab.show()
tf.reset_default_graph()
'''
声明变量
'''
#定义占位符
x = tf.placeholder(tf.float32, [None, 784])  #	MNIST数据集的维度是 28x28 = 784
y = tf.placeholder(tf.float32, [None, 10])   # 数字0-9
#定义学习参数
W = tf.Variable(tf.random_normal(([784, 10])))
b = tf.Variable(tf.zeros([10]))
'''
构建模型
'''
pred = tf.nn.softmax(tf.matmul(x, W) + b) #soft分类
'''
反向传播
'''
#损失函数
cost = tf.reduce_mean(-tf.reduce_sum(y*tf.log(pred),reduction_indices=1))
#定义参数
learning_rate = 0.01
#使用梯度下降法优化器
optimizer = tf.train.GradientDescentOptimizer(learning_rate).minimize(cost)

'''
训练模型
'''
training_epochs = 25
batch_size = 100
display_step = 1

saver = tf.train.Saver()
model_path = 'log/521model.ckpt'
#启动session
with tf.Session() as sess:
	sess.run(tf.global_variables_initializer())
	#启动循环训练
	for epoch in range(training_epochs):
		avg_cost = 0
		total_batch = int(mnist.train.num_examples/batch_size)
		#循环所有数据集
		for i in range(total_batch):
			batch_xs,batch_ys = mnist.train.next_batch(batch_size)
			#运行优化器
			_, c = sess.run([optimizer, cost], feed_dict={x:batch_xs,y:batch_ys})

			#计算平均loss值
			avg_cost += c / total_batch
		#显示训练中的详细信息
		if(epoch+1) % display_step == 0:
			print('Epoch:', '%04d' % (epoch+1), 'cost=','{:.9f}'.format(avg_cost))
	print('Finished!')

	'''
	测试模型
	'''
	correct_prediction = tf.equal(tf.argmax(pred, 1), tf.argmax(y, 1))
	#计算准确率
	accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
	print('Accuracy:',accuracy.eval({x:mnist.test.images,y:mnist.test.labels}))
	print('correct_prediction',correct_prediction.eval({x:mnist.test.images,y:mnist.test.labels}))
	#保存模型
	saver_path = saver.save(sess,model_path)
	print('Model saved in file: %s' % saver_path)
