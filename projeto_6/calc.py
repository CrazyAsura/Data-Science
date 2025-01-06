import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

df = pd.read_excel('C:/Users/Leon/Documents/Desenvolvimento de Web/Aprendizado/ciencia_de_dados/projeto_6/dados_vendas.xlsx')

df['Receita_Total'] = df['Quantidade'] * df['Preco_Unitario']

print(df)

df['Ano'] = pd.to_datetime(df['Data']).dt.year
df['Mes'] = pd.to_datetime(df['Data']).dt.month

X = df[['Ano', 'Mes']]
y = df['Receita_Total']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

modelo = LinearRegression()
modelo.fit(X_train, y_train)

y_pred = modelo.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
print(f"Erro Quadrático Médio (MSE): {mse}")

plt.figure(figsize=(10, 6))
plt.plot(y_test.values, label='Vendas Reais')
plt.plot(y_pred, label='Vendas Previstas')
plt.legend()
plt.title('Vendas Reais vs. Vendas Previstas')
plt.xlabel('Tempo')
plt.ylabel('Receita Total')
plt.savefig('grafico_vendas.png')
plt.show()

df['Vendas_Previstas'] = modelo.predict(X)

df.to_excel('Resultados_Previsão.xlsx', index=False)
print("Resultados salvos em Resultados_Previsão.xlsx")