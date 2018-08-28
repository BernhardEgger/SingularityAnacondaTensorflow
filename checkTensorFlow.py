import tensorflow as tf
tf.__version__
hello = tf.constant('Hello, TensorFlow!')
sess = tf.Session()
print(sess.run(hello))

from tensorflow.python.client import device_lib
device_lib.list_local_devices()
