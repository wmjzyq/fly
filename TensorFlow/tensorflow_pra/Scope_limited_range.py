import tensorflow as tf

with tf.variable_scope("scope1") as sp:
	var1 = tf.get_variable('v', [1])
#
# print('sp:',sp.name)
# print('var1:', var1.name)
#
# with tf.variable_scope('scope2'):
# 	var2 = tf.get_variable("v", [1])
#
# 	with tf.variable_scope(sp) as sp1:
# 		var3 = tf.get_variable('v3', [1]) #scope不会限制 v3
# print('sp1:', sp1.name)
# print('var2:', var2.name)
# print('var3:', var3.name)

"""
name_scope
"""
# with tf.variable_scope('scope'):
# 	with tf.name_scope('bar'):
# 		v = tf.get_variable('v', [1])
# 		x = 1.0 + v
# print('v:', v.name)                   #v是变量不会受到限制
# print('x.op:', x.op.name)             #x.op是操作会受到name_scope的限制

"""
name_scope 空字符返回顶层
"""
print('----------------------------------------------')
with tf.variable_scope('scope2'):
	var2 = tf.get_variable('v', [1])

	with tf.variable_scope(sp) as sp1:
		var3 = tf.get_variable('v3', [1])

		with tf.variable_scope(''):
			var4 = tf.get_variable('v4', [1])

with tf.variable_scope('scope'):
	with tf.name_scope('bar'):
		v = tf.get_variable('v', [1])
		x = 1.0 + v
		with tf.name_scope(''):
			y = 1.0 + v
print('var4:', var4.name) #variable_scope多一层//
print("y.op:", y.op.name) #name_scope 返回顶层
