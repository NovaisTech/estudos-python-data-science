import pandas as pd


#Criando um dicionário para meus estudos (simulação FCC)

dados_estudo = {  
    'Materia': ['Português', 'Direito Administrativo', 'BAnco de Dados', 'Python' ],
    'Questoes_Respondida': [20, 15, 30, 10],
    'Acertos': [16, 12, 25, 9]
}

# Transformando em um DataFrame (Tabela do Pandas)

df = pd.DataFrame(dados_estudo)

# Calculando a porcentagem de acertos
df['Percentual_%'] = (df['Acertos'] / df['Questoes_Respondida']) * 100

print("---Desempenhho Simulado FCC (NovaisTech) ---")
print(df)

# Filtrando matérias com aproveitamento acima de 80%
excelentes = df[df['Percentual_%'] >= 80]
print("\nMatérias com excelente aproveitamento (Foco FCC):")
print(excelentes['Materia'].tolist())
