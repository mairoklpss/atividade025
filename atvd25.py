# Enunciado: Crie um programa que receba a nota de 5 alunos e exiba quantos foram aprovados (nota maior ou igual a 7).
alunosAprovados = 0 

for i in range(1, 6):
    nota = float(input("digite a nota do aluno: "))
    
    if nota >= 7:
        alunosAprovados += 1
        
print (f"dos 5 alunos, {alunosAprovados} foram aprovados.")


    