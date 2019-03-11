import tensorflow as tf
# Use eager execution to embrace the upcoming tensorflow 2.0.
tf.enable_eager_execution()

x = tf.constant(4.5)
m = tf.multiply(x, x)
print("hello world {}".format(m))
