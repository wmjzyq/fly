import numpy_pra as np
import tensorflow as tf
c = tf.constant(0.0)

g = tf.Graph()
with g.as_default():
	c1 = tf.constant(0.0)
	print(c1.graph)
	print(c.graph)
	a = tf.get_default_graph()
	print(a)