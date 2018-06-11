import tensorflow as tf
sess = tf.Session()
a = tf.constant(5)
b = tf.constant(7)
print(sess.run(a+b))
sess.close()