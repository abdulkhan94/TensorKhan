import silence_tensorflow.auto
import tensorflow as tf

x1 = tf.constant([1, 2, 3, 4, 9])
x2 = tf.constant([5, 6, 7, 8, 2])

result = tf.multiply(x1, x2)

sess = tf.Session()

print(sess.run(result))

sess.close()
