import pandas as pd

# Exemplo de dados de vendas
dados_vendas = {
    'Produto': ['Produto A', 'Produto B', 'Produto C', 'Produto A', 'Produto B', 'Produto C'],
    'Quantidade Vendida': [150, 120, 200, 180, 130, 220],
    'Receita': [3000, 2400, 5000, 3600, 2600, 5500],
    'Região': ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'São Paulo', 'Rio de Janeiro', 'Belo Horizonte'],
    'Data': ['01/2025', '01/2025', '01/2025', '02/2025', '02/2025', '02/2025']
}

# Criação do DataFrame
df = pd.DataFrame(dados_vendas)

# Prompt 1: Tendências gerais de vendas
def gerar_tendencias(df):
    tendencia_produtos = df.groupby('Produto').agg({'Quantidade Vendida': 'sum', 'Receita': 'sum'}).reset_index()
    tendencia_produtos = tendencia_produtos.sort_values(by='Quantidade Vendida', ascending=False)
    return tendencia_produtos

# Prompt 2: Produto mais vendido
def produto_mais_vendido(df):
    produto_vendido = df.groupby('Produto').agg({'Quantidade Vendida': 'sum', 'Receita': 'sum'}).reset_index()
    produto_vendido = produto_vendido.sort_values(by='Quantidade Vendida', ascending=False).iloc[0]
    return produto_vendido

# Prompt 3: Desempenho de vendas por região
def desempenho_por_regiao(df):
    desempenho_regiao = df.groupby('Região').agg({'Quantidade Vendida': 'sum', 'Receita': 'sum'}).reset_index()
    return desempenho_regiao

# Gerar insights
tendencias = gerar_tendencias(df)
produto_top = produto_mais_vendido(df)
desempenho = desempenho_por_regiao(df)

# Exibindo os resultados
print("Tendências Gerais de Vendas:")
print(tendencias)

print("\nProduto Mais Vendido:")
print(produto_top)

print("\nDesempenho de Vendas por Região:")
print(desempenho)
