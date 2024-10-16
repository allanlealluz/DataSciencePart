import random

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

# Exibindo os resultados
print("Feedbacks:")
for aula, feedback in feedbacks.items():
    print(f"{aula}:")
    for f in feedback:
        print(f"  {f['nome']} - {f['pergunta']}: {f['resposta']}")

print("\nProgresso:")
for aula, prog in progresso.items():
    print(f"{aula}:")
    for p in prog:
        print(f"  {p['nome']} - Progresso: {p['progresso']}%")
