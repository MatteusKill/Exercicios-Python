nomeAluno = str (input("Digite o nome do aluno: "))
nomeDisciplina = input ("Digite o nome da disciplina lecionada: ")
notaP1 = float (input ("Digite a nota da primeira prova: "))
notaP2 = float (input ("Digite a nota da segunda prova: "))
notaP3 = float (input ("Digite a nota da terceira prova: "))

media = (notaP1 + notaP2 + notaP3) / 3

print("Aluno: ", nomeAluno)
print("Disciplina: ", nomeDisciplina)
print(f"Media da disciplina: {media:.2f}")