import pandas as pd

# Atualize o caminho do arquivo conforme a localização no seu sistema
df = pd.read_excel('C:/Users/Leon/Documents/Desenvolvimento de Web/Aprendizado/ciencia_de_dados/projeto_2/vendas.xlsx')

print('Dados Originais')
print(df.head())

df['Quantidade'] = pd.to_numeric(df['Quantidade'], errors='coerce')
df['PrecoUnitario'] = pd.to_numeric(df['PrecoUnitario'], errors='coerce')

df['ValorTotal'] = df['Quantidade'] * df['PrecoUnitario']

print("\nDados com a coluna 'ValorTotal' adicionada:")
print(df.head())

mean = df['ValorTotal'].mean()
median = df['ValorTotal'].median()
mode = df['ValorTotal'].mode()[0]

print("\nEstatísticas:")
print(f"Média do 'ValorTotal': {mean}")
print(f"Mediana do 'ValorTotal': {median}")
print(f"Moda do 'ValorTotal': {mode}")