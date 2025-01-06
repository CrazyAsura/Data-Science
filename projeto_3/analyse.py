import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

df = pd.read_csv('C:/Users/Leon/Documents/Desenvolvimento de Web/Aprendizado/ciencia_de_dados/projeto_3/vendas_historicas.csv')

df['Data'] = pd.to_datetime(df['Data'])
df['Ano'] = df['Data'].dt.year
df['Mês'] = df['Data'].dt.month
df['Dia_da_Semana'] = df['Data'].dt.dayofweek

X = df[['Ano', 'Mês', 'Dia_da_Semana']]
y = df['Vendas']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

plt.figure(figsize=(10, 6))
plt.plot(y_test.values, label='Valores Reais')
plt.plot(y_pred, label='Vendas Previstas')
plt.legend()
plt.title('Comparação entre Valores Reais e Previstos')
plt.show()