import tensorflow as tf
from keras import layers, models
from keras.datasets import mnist
import matplotlib.pyplot as plt

(x_train, y_train), (x_test, y_test) = mnist.load_data()

x_train, x_test = x_train / 255.0, x_test / 255.0

plt.imshow(x_train[0], cmap='gray')
plt.title(f'label: {y_train[0]}')
plt.show()

# Modelo corrigido
model = models.Sequential([
    layers.Input(shape=(784,)),  # Forma correta de definir o input
    layers.Dense(128, activation='relu'),
    layers.Dense(10, activation='softmax')  # Corrigido 'softmax'
])

model.summary()

model.compile(optimizer='adm',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(x_train, y_train, epochs=5)

test_loss, test_acc = model.evaluate(x_test, y_test)
print(f'\nTest accuracy: {test_acc}')

predictions = model.predict(x_test)

plt.imshow(x_test[0], cmap='gray')
plt.title(f'Predicted: {tf.argmax(predictions[0])}')
plt.show()