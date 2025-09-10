nomeAluno = input("Digite o nome do aluno: ")
disciplina = input("Digite o nome da disciplina: ")

nota1 = float(input("Digite a nota da Prova 1: "))
nota2 = float(input("Digite a nota da Prova 2: "))
nota3 = float(input("Digite a nota da Prova 3: "))

media = (nota1 + nota2 + nota3) / 3

if (media >= 6.0):
    situacao = "Aprovado"
else:
    situacao = "Reprovado"
"\n"
print("--------------------------")
print("Aluno: ", nomeAluno)
print("Disciplina: " + disciplina)
print(f"Nota da Prova 1: {nota1}")
print(f"Nota da Prova 2: {nota2}")
print(f"Nota da Prova 3: {nota3}")
print(f"Média Final: {media:.2f}")
print("Situação: ", situacao)