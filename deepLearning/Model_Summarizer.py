import tensorflow as tf

# Define your model architecture
model = YourModel()

# Define a checkpoint object
checkpoint = tf.train.Checkpoint(model=model)

# Load the weights from the checkpoint file
checkpoint.restore("path/to/your/checkpoint/directory/ckpt.data")
