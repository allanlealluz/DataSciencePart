import random
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Função para simular dados de feedbacks
def generate_feedbacks(num_aulas, num_alunos):
    feedbacks = {}
    for aula_id in range(num_aulas):
        feedbacks[f'Aula {aula_id + 1}'] = [
            {
                'nome': f'Aluno {random.randint(1, num_alunos)}',
                'pergunta': f'Pergunta {random.randint(1, 5)}',
                'resposta': random.choice(['Ótimo', 'Bom', 'Regular', 'Ruim'])
            }
            for _ in range(random.randint(1, num_alunos))
        ]
    return feedbacks

# Função para simular progresso
def generate_progresso(num_aulas, num_alunos):
    progresso = {}
    for aula_id in range(num_aulas):
        progresso[f'Aula {aula_id + 1}'] = [
            {
                'nome': f'Aluno {random.randint(1, num_alunos)}',
                'progresso': random.randint(0, 100)
            }
            for _ in range(num_alunos)
        ]
    return progresso

# Simulando dados
num_aulas = 3
num_alunos = 10
feedbacks = generate_feedbacks(num_aulas, num_alunos)
progresso = generate_progresso(num_aulas, num_alunos)

# Agregando dados para análise
alunos_data = {}
for aula in progresso:
    for aluno in progresso[aula]:
        nome = aluno['nome']
        if nome not in alunos_data:
            alunos_data[nome] = {'progresso': [], 'feedbacks': 0}
        alunos_data[nome]['progresso'].append(aluno['progresso'])
        alunos_data[nome]['feedbacks'] += len([f for f in feedbacks[aula] if f['nome'] == nome])

# Preparando dados para clustering
X = []
nomes_alunos = []
for nome, data in alunos_data.items():
    progresso_medio = np.mean(data['progresso']) if data['progresso'] else 0
    feedback_count = data['feedbacks']
    X.append([progresso_medio, feedback_count])
    nomes_alunos.append(nome)

X = np.array(X)

# Aplicando K-Means para encontrar perfis de alunos
kmeans = KMeans(n_clusters=3, random_state=42)
labels = kmeans.fit_predict(X)

# Visualizando os resultados
plt.figure(figsize=(10, 6))
scatter = plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='viridis', marker='o', edgecolor='k', s=100)

# Centróides
centroids = kmeans.cluster_centers_
plt.scatter(centroids[:, 0], centroids[:, 1], c='red', marker='X', s=200, label='Centroides')

# Adicionando anotações
for i, nome in enumerate(nomes_alunos):
    plt.annotate(nome, (X[i, 0], X[i, 1]), fontsize=9, ha='right')

plt.title('Perfis de Alunos Baseados em Progresso e Feedbacks')
plt.xlabel('Progresso Médio (%)')
plt.ylabel('Quantidade de Feedbacks')
plt.grid()
plt.legend()
plt.show()

# Exibindo os dados dos alunos com seus rótulos de cluster
for i, nome in enumerate(nomes_alunos):
    print(f"{nome}: Cluster {labels[i]}")
