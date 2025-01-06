"""
This script performs the following tasks:
1. Generates a sample dataset of sales data for different regions and products.
2. Writes the dataset to an Excel file named 'vendas_agrupadas.xlsx'.
3. Reads the data from the Excel file and performs aggregation operations to calculate the total sales, average sales, total cost, and average cost for each region and product.
4. Prints the aggregated data.
5. Generates a bar chart of the total sales by region and product, and saves the chart to a file named 'grafico_vendas_totais.png'.
"""
import pandas as pd
import matplotlib.pyplot as plt

# Criar os dados
dados = {
    'Regiao': ['Norte', 'Norte', 'Sul', 'Sul', 'Leste', 'Leste', 'Oeste', 'Oeste', 'Norte', 'Sul'],
    'Produto': ['A', 'B', 'A', 'B', 'A', 'B', 'A', 'B', 'A', 'B'],
    'Mes': ['Janeiro', 'Janeiro', 'Fevereiro', 'Fevereiro', 'Março', 'Março', 'Abril', 'Abril', 'Maio', 'Maio'],
    'Vendas': [1200, 800, 1000, 900, 1500, 1100, 1300, 700, 1600, 950],
    'Custo': [500, 400, 600, 550, 800, 700, 700, 300, 900, 450]
}

df = pd.DataFrame(dados)

df.to_excel('vendas_agrupadas.xlsx', index=False)
print("Arquivo 'vendas_agrupadas.xlsx' criado com sucesso!")

df = pd.read_excel('vendas_agrupadas.xlsx')

agrupado = df.groupby(['Regiao', 'Produto']).agg({
    'Vendas': ['sum', 'mean'],
    'Custo': ['sum', 'mean']
}).reset_index()

agrupado.columns = ['Regiao', 'Produto', 'Vendas_Totais', 'Vendas_Media', 'Custo_Total', 'Custo_Medio']

print(agrupado)

plt.figure(figsize=(10, 6))
for produto in agrupado['Produto'].unique():
    data_produto = agrupado[agrupado['Produto'] == produto]
    plt.bar(data_produto['Regiao'], data_produto['Vendas_Totais'], label=produto)
    plt.title('Vendas Totais por Região e Produto')
plt.xlabel('Região')
plt.ylabel('Vendas Totais')
plt.legend()
plt.savefig('grafico_vendas_totais.png')
plt.show()