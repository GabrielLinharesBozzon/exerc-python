#-*-coding:utf8-*-
#11)As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
#Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
#salários até R$ 280,00 (incluindo) : aumento de 20%
#salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
#salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
#salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
#o salário antes do reajuste;
#o percentual de aumento aplicado;
#o valor do aumento;
#o novo salário, após o aumento.
S=float(input("Digite seu salario:\n"))
if S <= 280:
    print("Seu salaraio é de:",S,"\nO aumento foi de 20%\nO acrecimo foi de:",((S/100)*20),"R$\nTotalizando:",(S+((S/100)*20)))
elif S >=280 and S<=700:
    print("Seu salaraio é de:",S,"\nO aumento foi de 15%\nO acrecimo foi de:",((S/100)*15),"R$\nTotalizando:",(S+((S/100)*15)))
elif S >= 700 and S <= 1500:
    print("Seu salaraio é de:",S,"\nO aumento foi de 10%\nO acrecimo foi de:",((S/100)*10),"R$\nTotalizando:",(S+((S/100)*10)))   
elif S >= 1500:
    print("Seu salaraio é de:",S,"\nO aumento foi de 5%\nO acrecimo foi de:",((S/100)*5),"R$\nTotalizando:",(S+((S/100)*5)))
else:
    print("Valor não aceito")    