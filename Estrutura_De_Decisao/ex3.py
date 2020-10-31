#-*-coding:utf8-*-
#3)Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
p=str(input("Confirme o sexo :\n Se for Masculino 'M' ou se for Feminino 'F':\n").upper())
if p == 'F':
    print("Feminino")
elif p == 'M':
    print("Masculino")
else:
    print("Sexo Inválido")