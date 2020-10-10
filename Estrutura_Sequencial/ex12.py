#12)Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
#Para homens: (72.7*h) - 58
#Para mulheres: (62.1*h) - 44.7
h=float(input("Sua altura:\n"))
S=input("Digite o seu sexo\n'M'Para homem.\n'F'Para feminino.\n")
if S=='M':
    print("Seu peso é de :",((72.7*h)-58))
elif S=='F':
    print("Seu peso é de :",((62.1*h)-44.7)) 
else:
    print("Sexo não aceito")



