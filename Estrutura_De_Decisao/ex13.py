#-*-coding:utf8-*-
#13)Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.
S=int(input("Digite um número e o programa vai responder qual dia da semana corresponde: \n"))
if S==1:
    print("você digitou:\n",S,"representa Domingo")
elif S==2:
    print("você digitou:\n",S,"representa Segunda-feira ")
elif S==3:
    print("você digitou:\n",S,"representa terça-feira")
elif S==5:
    print("você digitou:\n",S,"representa quarta-feira ") 
elif S==6:
    print("você digitou:\n",S,"representa quinta-feira")
elif S==7:
    print("você digitou:\n",S,"representa Sexta-feira ")
elif S==8:
    print("você digitou:\n",S,"representa Sabado")              
else:    
    print("O valor digitado não é aceito") 
