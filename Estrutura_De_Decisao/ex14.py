#14)Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
 # Média de Aproveitamento  Conceito
 # Entre 9.0 e 10.0        A
 # Entre 7.5 e 9.0         B
 # Entre 6.0 e 7.5         C
 # Entre 4.0 e 6.0         D
 # Entre 4.0 e zero        E
#O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito for D #ou E.
N1=float(input("Digite a primeira nota:"))
N2=float(input("Digite a segunda  nota:"))
R=(float((N1+N2)/2))
print(R)
if R >= 9 and R <= 10:
    print("A")
elif R >= 7.5 and R <= 8.9:
    print("B")
elif R >= 6 and R <= 7.5:
    print("C")
elif R >= 4 and R <= 6:
    print("D")
elif R >= 0 and R <= 4:
    print("E")
