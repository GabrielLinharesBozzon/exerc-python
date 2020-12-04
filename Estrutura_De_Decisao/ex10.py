#-*-coding:utf8-*-
#10)Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.
n =input("Para o periodo matutino aperte M\nPara o periodo Vespertino aperte V\nPara o periodo Noturno aperte N\n")
if n=='M':
    print("Bom dia")
elif n=='V':
    print("Boa tarde") 
elif n=='N':      
    print("Boa noite")
else:
    print("Valor não invalido")