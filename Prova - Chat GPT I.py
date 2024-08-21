soma_turma = 0
lista_nomes = []
lista_notas1 = []
lista_notas2 = []
lista_notas3 = []
lista_status = []
soma_notas = []
lista_media  = []

n_aln = int(input("Digite quantos alunos vão ser registrados: "))

for i in range (n_aln):
    nome = input("Nome do aluno(a): ")
    lista_nomes.append(nome)
    nota1 = int(input("Digite a primeira nota: "))
    lista_notas1.append(nota1)
    nota2 = int(input("Digite a segunda nota: "))
    lista_notas2.append(nota2)
    nota3 = int(input("Digite a terceira nota: "))
    lista_notas3.append(nota3)
    print()
    soma_notas = nota1 + nota2 + nota3
    media_notas = soma_notas / 3
    media_notas = f"{media_notas:.2f}"
    lista_media.append(media_notas)

    if media_notas >= "7":
        status = "Aprovado"
    else:
        status = "Reprovado"
    lista_status.append(status)
    
    soma_turma += nota1 + nota2 + nota3
media_turma = soma_turma / n_aln
media_turma = f"{media_turma:.2f}"

print("Informações:")

for i in range (n_aln):
   print(f"Nome: {lista_nomes[i]}")
   print(f"Nota1 = {lista_notas1[i]}")
   print(f"Nota2 = {lista_notas2[i]}")
   print(f"Nota3 = {lista_notas3[i]}")
   print(f"Média = {lista_media[i]}")
   print(f"Status: {lista_status[i]}")
   print()


print(f"Média da turma: {media_turma}")