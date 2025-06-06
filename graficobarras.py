import matplotlib.pyplot as plt
import pandas as pd

# ===== Dados detalhados =====
dados = {
    'Categoria': [
        'Mais de 6 anos', 'Mais de 6 anos', 'Mais de 6 anos', 'Mais de 6 anos', 'Mais de 6 anos',
        '5 anos', '5 anos', '5 anos', '5 anos', '5 anos',
        'Lançamentos', 'Lançamentos', 'Lançamentos', 'Lançamentos', 'Lançamentos'
    ],
    'Jogo': [
        'Fortnite', 'GTA 5', 'Rainbow 6', 'Roblox', 'Minecraft',
        'COD Warfare 3', 'EA Sports FC', 'Apex Legends', 'NBA 2K24', 'Elden Ring',
        'COD OPS 6', 'EA Sports FC 24', 'NBA 2K25', 'EA College Football', 'Helldrives 2'
    ],
    'Popularidade (%)': [
        13.8, 4.4, 2.8, 2.8, 2.1,
        8.4, 7.6, 2.9, 2.2, 0.5,
        3.9, 2.5, 1.0, 0.9, 0.7
    ]
}

df = pd.DataFrame(dados)

# ===== Gráfico de Barras =====
plt.figure(figsize=(12, 8))
cores = {
    'Mais de 6 anos': '#1f77b4',
    '5 anos': '#ff7f0e',
    'Lançamentos': '#2ca02c'
}

for categoria in df['Categoria'].unique():
    subset = df[df['Categoria'] == categoria]
    plt.bar(subset['Jogo'], subset['Popularidade (%)'], 
            color=cores[categoria], label=categoria)

plt.xlabel('Jogos', fontsize=12)
plt.ylabel('Popularidade (%)', fontsize=12)
plt.title('Jogos Mais Populares de Playstation em 2024 - Gráfico de Barras', fontsize=14)
plt.xticks(rotation=45, ha='right')

for index, row in df.iterrows():
    plt.text(row['Jogo'], row['Popularidade (%)'] + 0.1, 
             f"{row['Popularidade (%)']}%", ha='center', fontsize=9)

plt.legend(title='Categoria')
plt.tight_layout()
plt.savefig('jogos_playstation_barras.png', dpi=300)
plt.show()
print("✅ Gráfico de barras salvo como 'jogos_playstation_barras.png'")

# ===== Gráfico de Pizza =====
soma_por_categoria = df.groupby('Categoria')['Popularidade (%)'].sum()
cores_pizza = [cores[categoria] for categoria in soma_por_categoria.index]

plt.figure(figsize=(8, 8))
plt.pie(soma_por_categoria, labels=soma_por_categoria.index, autopct='%1.1f%%', 
        startangle=90, colors=cores_pizza, wedgeprops={'edgecolor': 'white'})

plt.title('Distribuição da Popularidade por Categoria - Gráfico de Pizza', fontsize=14)
plt.savefig('jogos_playstation_pizza.png', dpi=300)
plt.show()
print("✅ Gráfico de pizza salvo como 'jogos_playstation_pizza.png'")

# ===== Gráfico de Linhas - Evolução temporal =====

# Criar dados de evolução
anos = [2020, 2021, 2022, 2023, 2024]
evolucao_dados = {
    'Ano': anos * 5,  # 5 jogos
    'Jogo': ['Fortnite']*5 + ['GTA 5']*5 + ['Minecraft']*5 + ['COD Warfare 3']*5 + ['EA Sports FC']*5,
    'Popularidade (%)': [
        20, 18, 16, 15, 13.8,    # Fortnite
        6, 5.5, 5, 4.8, 4.4,     # GTA 5
        3, 2.9, 2.5, 2.3, 2.1,   # Minecraft
        0, 0, 4, 6, 8.4,         # COD Warfare 3 (subiu com lançamento)
        0, 0, 3, 5, 7.6          # EA Sports FC (aumentando)
    ]
}

df_evolucao = pd.DataFrame(evolucao_dados)

# Criar o gráfico de linhas
plt.figure(figsize=(10, 6))

for jogo in df_evolucao['Jogo'].unique():
    subset = df_evolucao[df_evolucao['Jogo'] == jogo]
    plt.plot(subset['Ano'], subset['Popularidade (%)'], marker='o', label=jogo)

plt.xlabel('Ano', fontsize=12)
plt.ylabel('Popularidade (%)', fontsize=12)
plt.title('Evolução da Popularidade de Jogos (2020-2024)', fontsize=14)
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig('jogos_playstation_linhas.png', dpi=300)
plt.show()

print("✅ Gráfico de linhas salvo como 'jogos_playstation_linhas.png'")
