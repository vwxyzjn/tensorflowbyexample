import tensorflow as tf
tf.enable_eager_execution()

params = tf.constant([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
indices = [0, 2]
# tf.gather() snatches the slices in `params` according to `indices`
print(tf.gather(params, indices))
