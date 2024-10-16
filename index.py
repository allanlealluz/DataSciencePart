import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Gerando notas fictícias para 100 alunos
np.random.seed(42)
notas_matematica = np.random.randint(50, 101, size=100)  # Notas de Matemática entre 50 e 100
notas_ciencias = np.random.randint(50, 101, size=100)    # Notas de Ciências entre 50 e 100

# Combinando as notas em um array 2D
X = np.array(list(zip(notas_matematica, notas_ciencias)))

# Aplicando K-Means para encontrar 3 grupos de alunos
kmeans = KMeans(n_clusters=3, random_state=42)
kmeans.fit(X)
labels = kmeans.labels_

# Visualizando os resultados
plt.figure(figsize=(10, 6))
plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='viridis', marker='o', edgecolor='k', s=100)

# Centróides
centroids = kmeans.cluster_centers_
plt.scatter(centroids[:, 0], centroids[:, 1], c='red', marker='X', s=200)

plt.title('Agrupamento de Alunos por Notas em Matemática e Ciências')
plt.xlabel('Notas em Matemática')
plt.ylabel('Notas em Ciências')
plt.grid()
plt.xlim(40, 110)
plt.ylim(40, 110)
plt.show()
