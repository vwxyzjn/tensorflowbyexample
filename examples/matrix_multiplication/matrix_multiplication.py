import tensorflow as tf
# Taken from https://www.tensorflow.org/guide/eager
# Eager execution works nicely with NumPy. NumPy operations accept tf.Tensor arguments. 
# TensorFlow math operations convert Python objects and NumPy arrays to tf.Tensor objects. 
# The tf.Tensor.numpy method returns the object's value as a NumPy ndarray.
tf.enable_eager_execution()
a = tf.constant([
    [1, 2],
    [3, 4]]
)
print(a)

# Broadcasting support
b = tf.add(a, 1)
print(b)

# Operator overloading is supported
print(a * b)

# Use NumPy values
import numpy as np

c = np.multiply(a, b)
print(c)
