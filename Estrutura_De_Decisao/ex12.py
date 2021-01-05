#-*-coding:utf8-*-
#12)Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
#Desconto do IR:
#Salário Bruto até 900 (inclusive) - isento
#Salário Bruto até 1500 (inclusive) - desconto de 5%
#Salário Bruto até 2500 (inclusive) - desconto de 10%
#Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.
#        Salário Bruto: (5 * 220)        : R$ 1100,00
#        (-)IR (5%)                      : R$   55,00  
#        (-)INSS(10%)                    : R$  110,00
#        FGTS (11%)                      : R$  121,00
#        Total de descontos              : R$  165,00
#        Salário Liquido                 : R$  935,00
def Cal():
 print("Salário Bruto:\nR$:",s)
if s >= 900:
    print("")
elif s >=900 and S<=1500:
    print("")
elif s >=1500 and S<=2500:
    print("")
elif s >=2500:
    print("")
    pass
op=int(input("Escolha as opções a baixo:\nOpção (1):\nCalcular o numero de horas e valor dela.\nOpção (2):\nEntrar com o valor direto."))
if op==1:
    print("Foi digitado opção(1)\nCalcular o numero de horas e valor dela.")
    v1=int(input("Digite o numeros de horas trabalhado:"))
    v2=int(input("Digite o cvalor delas:"))
    rest=v1*v2
    s1=Cal(rest)
elif op==2:
    print("Foi digitado opção(2)\nEntrar com o valor direto.")
    i=int(input("Digite o seu salario:\nR$"))
    s2=Cal(i)