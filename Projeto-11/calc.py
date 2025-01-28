import pandas as pd          # Manipulação de dados em forma de DataFrame
import numpy as np           # Funções matemáticas, operações com arrays
import matplotlib.pyplot as plt # Visualização de dados (gráficos)
import seaborn as sns        # Visualização de dados mais avançada

from sklearn.model_selection import train_test_split  # Para dividir os dados em treino e teste
from sklearn.preprocessing import StandardScaler     # Para normalização dos dados
from keras import Sequential   # Keras para definir o modelo
from keras import layers       # Camadas da rede neural
from keras import callbacks, Dense, EarlyStopping  # Para evitar overfitting


df = pd.read_csv('clientes_telecom.csv')

print(df.head())

print(df.info())

print(df.describe)

df.fillna(df.mean(), inplace=True)

df = pd.get_dummies(df, drop_first=True)

X = df.drop('churn', axis=1)
y = df['churn']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

model = Sequential()

# Primeira camada densa (entrada)
model.add(Dense(units=64, activation='relu', input_dim=X_train.shape[1]))

# Segunda camada densa
model.add(Dense(units=32, activation='relu'))

# Camada de saída (resultado final)
model.add(Dense(units=1, activation='sigmoid'))

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Usando EarlyStopping para evitar overfitting
early_stopping = EarlyStopping(monitor='val_loss', patience=10, restore_best_weights=True)

# Treinando o modelo
history = model.fit(X_train, y_train, epochs=100, batch_size=32, validation_split=0.2, callbacks=[early_stopping])

loss, accuracy = model.evaluate(X_test, y_test)

print(f"Loss: {loss}")
print(f"Acurácia: {accuracy}")

plt.figure(figsize=(12, 6))

# Acurácia
plt.subplot(1, 2, 1)
plt.plot(history.history['accuracy'], label='Acurácia de treino')
plt.plot(history.history['val_accuracy'], label='Acurácia de validação')
plt.title('Acurácia durante o treinamento')
plt.xlabel('Epochs')
plt.ylabel('Acurácia')
plt.legend()

# Perda
plt.subplot(1, 2, 2)
plt.plot(history.history['loss'], label='Perda de treino')
plt.plot(history.history['val_loss'], label='Perda de validação')
plt.title('Perda durante o treinamento')
plt.xlabel('Epochs')
plt.ylabel('Perda')
plt.legend()

plt.show()
