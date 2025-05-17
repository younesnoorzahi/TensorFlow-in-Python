import tensorflow as tf

# Basic tensor operations
a = tf.constant(5)
b = tf.constant(3)
c = tf.add(a, b)  # or simply a + b

# Neural network layers
model = tf.keras.Sequential([
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(10, activation='softmax')
])

# Automatic differentiation
with tf.GradientTape() as tape:
    y = model(x)
    loss = tf.keras.losses.sparse_categorical_crossentropy(y_true, y)
gradients = tape.gradient(loss, model.trainable_variables)