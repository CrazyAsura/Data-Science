import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('/Users/Leon/Documents/Desenvolvimento de Web/Aprendizado/ciencia_de_dados/projeto_2/vendas.xlsx')

print(df.head())

# Criando uma nova coluna 'ValorTotal'
df['ValorTotal'] = df['Quantidade'] * df['PrecoUnitario']

# Exibindo as primeiras linhas para ver as mudanças
print(df.head())

vendas_produto = df.groupby('Produto')['ValorTotal'].sum()

# Exibindo o total de vendas por produto
print(vendas_produto)

vendas_data = df.groupby('Data')['ValorTotal'].sum()

print(vendas_data)

vendas_produto.plot(kind='bar', color='skyblue', title='Vendas por Produto')
plt.ylabel('Valor Total')
plt.show()

vendas_data.plot(kind='line', color='green', marker='o', title='Vendas por Data')
plt.ylabel('Valor Total')
plt.xticks(rotation=45)
plt.show()

df.to_excel('vendas_com_valor_total.xlsx', index=False)

vendas_produto.to_excel('totais_vendas_produtos.xlsx')
