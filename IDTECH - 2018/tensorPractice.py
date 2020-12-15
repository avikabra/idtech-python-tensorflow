import tensorflow as tf

a = tf.placeholder(dtype=tf.float32, shape= None)

b = tf.placeholder(dtype=tf.float32, shape= None)

c = tf.constant(10, dtype=tf.float32)

operation = a * b + c

with tf.Session() as sess:
    print(sess.run(operation, feed_dict={a: 10, b: 13}))