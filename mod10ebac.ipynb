# Importação das bibliotecas necessárias
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregando o arquivo CSV em um DataFrame
df = pd.read_csv('ecommerce_preparados.csv')

# Análise exploratória dos dados
print(df.head())
print(df.info())
print(df.describe())

# Gráfico de Histograma
plt.figure(figsize=(8, 5))
sns.histplot(data=df, x='Nota', kde=True)
plt.title('Histograma')
plt.xlabel('Notas')
plt.ylabel('Frequência')
plt.show()

# Gráfico de Dispersão
plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x='Nota', y='Preço')
plt.title('Relação entre preço do produto e nota atribuída')
plt.xlabel('Nota')
plt.ylabel('Preço')
plt.show()

# Mapa de Calor
plt.figure(figsize=(10, 8))
corr = df.corr(method='pearson', min_periods=1, numeric_only=True)
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title('Correlação entre as variáveis')
plt.show()

# Gráfico de Barra
df['Temporada'] = df['Temporada'].str.replace('outono/inverno', 'outono-inverno', regex=False)
df['Temporada'] = df['Temporada'].str.replace('primavera/verão', 'primavera-verão', regex=False)
df['Temporada'] = df['Temporada'].str.replace('primavera-verão outono-inverno', 'não definido', regex=False)
df['Temporada'] = df['Temporada'].str.replace('primavera/verão/outono/inverno', 'não definido', regex=False)
df['Temporada'] = df['Temporada'].str.replace('2021', 'não definido', regex=False)
df['Temporada'] = df['Temporada'].str.replace('primavera/verão outono/inverno', 'não definido', regex=False)
df['Temporada'] = df['Temporada'].str.replace('primavera-verão/outono-inverno', 'não definido', regex=False)
df['Temporada'] = df['Temporada'].str.replace('primavera-verão - outono-inverno', 'não definido', regex=False)
sns.countplot(x='Qtd_Vendidos', hue='Temporada', data=df)
plt.title('Quantidade de vendas por temporada')
plt.xlabel('Temporada')
plt.ylabel('Quantidade vendida')
plt.legend(title='Temporada')
plt.show()

# Gráfico de Pizza
plt.figure(figsize=(6, 6))
df['Temporada'].value_counts().plot(kind='pie', autopct='%1.1f%%')
plt.title('Temporadas de maior procura')
plt.show()

# Gráfico de Densidade
plt.figure(figsize=(8, 5))
sns.kdeplot(data=df, x='Nota')
plt.title('Densidade de notas atribuídas')
plt.xlabel('Nota')
plt.ylabel('Densidade')
plt.show()

# Gráfico de Regressão
plt.figure(figsize=(8, 5))
sns.regplot(data=df, x='Nota', y='Desconto')
plt.title('Regressão entre nota atribuída e desconto')
plt.xlabel('Nota')
plt.ylabel('Desconto')
plt.show()
