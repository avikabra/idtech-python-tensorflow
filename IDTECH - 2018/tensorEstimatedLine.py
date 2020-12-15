import tensorflow as tf

#clear the graph
tf.reset_default_graph()

#placeholders
input_data = tf.placeholder(dtype=tf.float32, shape=None)
output_data = tf.placeholder(dtype=tf.float32, shape=None)

#variables
slope = tf.Variable(0.5, dtype=tf.float32)
intercept = tf.Variable(0.1, dtype=tf.float32)

#method
model_operation = slope * input_data + intercept
error = model_operation - output_data
squared_error = tf.square(error)
loss = tf.reduce_mean(squared_error)

#session run
init = tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init)

#still in progress