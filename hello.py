import tensorflow as tf
import numpy as np

hi = tf.constant('hello tensorflow')
sess = tf.Session()

print(sess.run(hi))
