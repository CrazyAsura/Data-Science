"""
This script performs the following tasks:
1. Reads a CSV file containing sales data into a Pandas DataFrame.
2. Calculates the total value of each sale by multiplying the quantity and unit price.
3. Groups the sales data by product and calculates the total sales value for each product.
4. Groups the sales data by date and calculates the total sales value for each date.
5. Generates two plots: one showing the total sales value for each product, and one showing the total sales value over time.
"""
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('C:/Users/Leon/Documents/Desenvolvimento de Web/Aprendizado/ciencia_de_dados/projeto_1/vendas.csv')

print(df.head())

df['ValorTotal'] = df['Quantidade'] * df['PrecoUnitario']

print(df)

vendas_produto = df.groupby('Produto')['ValorTotal'].sum()

#print(vendas_produto)

# Calculando o total de vendas por data
vendas_data = df.groupby('Data')['ValorTotal'].sum()

# Exibindo o total de vendas por data
#print(vendas_data)

vendas_produto.plot(kind='bar', color='skyblue', title='Vendas por Produto')
plt.ylabel('Valor Total')
plt.show()

vendas_data.plot(kind='line', color='green', marker='o', title='Vendas por Data')
plt.ylabel('Valor Total')
plt.xticks(rotation=45)
plt.show()

#df.to_csv('vendas_com_valor_total.csv', index=False)

#vendas_produto.to_csv('totais_vendas_produtos.csv')