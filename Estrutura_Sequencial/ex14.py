#14)Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
#salário bruto.
#quanto pagou ao INSS.
#quanto pagou ao sindicato.
#o salário líquido.
#calcule os descontos e o salário líquido, conforme a tabela abaixo:
#+ Salário Bruto : R$
#- IR (11%) : R$
#- INSS (8%) : R$
#- Sindicato ( 5%) : R$
#= Salário Liquido : R$
#Obs.: Salário Bruto - Descontos = Salário Líquido.
n1=float(input("Quanto você ganha por hora:\n"))
n2=int(input("Quanto horas são trabalhadas por dia:\n"))
n3=(int(input("Quantos dia são trabalhados por semana:\n"))*4)
T=(n1*n2*n3)#Total bruto do salario
P=(T/100)#Porcento do salario
print("O salario bruto é de:",T,
"\nIR                (11%) : R$",(P*11),#Imposto de renda 
"\nINSS              ( 8%) : R$",(P*8),#Inss
"\nSindicato         ( 5%) : R$",(P*5),#Taxa Sindical
"\nSalário Liquido         : R$",(T-((P*5)+(P*8)+(P*11))))#Calculo do Salario liquido