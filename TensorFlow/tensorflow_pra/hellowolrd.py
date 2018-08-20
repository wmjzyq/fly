import tensorflow as tf
hw = tf.constant('hello world! I love TensorFlow!')
sess = tf.Session()
#运行Graph（计算图）
print(sess.run(hw))
sess.close()