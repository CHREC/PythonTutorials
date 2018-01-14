#  Acquire MNIST data
from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)

#  Import TensorFlow
import tensorflow as tf

#  Create symbolic variables:
x = tf.placeholder(tf.float32, [None, 784])  # values in each of the pixels
#  the placeholder value will be inputted when using TensorFlow
#  None indicates that it can be of any value (so any number of images can be inputted)

W = tf.Variable(tf.zeros([784, 10]))  # weightage for each of the x
b = tf.Variable(tf.zeros([10]))  # initial bias
#  the variable is a modifiable tensor

# Implement model / define it:
y = tf.nn.softmax(tf.maymul(x, W) + b)

# Cross Entropy
y_ = tf.placeholder(tf.float32, [None, 10])
cross_entropy = tf.reduce_mean(-tf.reduce_sum(y_ * tf.log(y), reduction_indices=[1]))

# Training model
train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)

# Launch in Interactive Session
sess = tf.InteractiveSession()
tf.global_variables_initializer().run()

for _ in range(1000):  # 1000 steps
    batch_xs, batch_ys = mnist.train.next_batch(100)
    sess.run(train_step, feed_dict={x: batch_xs, y_: batch_ys})

# Evaluating Model
correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(y_, 1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
print(sess.run(accuracy, feed_dict={x: mnist.test.images, y_: mnist.test.labels}))
