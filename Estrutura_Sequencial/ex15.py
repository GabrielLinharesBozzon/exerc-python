#-*-coding:utf8-*-#
# 15)Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
# Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
# Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
# comprar apenas latas de 18 litros;
# comprar apenas galões de 3,6 litros;
# misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.
#----------------------------------------------------------------------------------------------------------------------------------------------------------------#
l1 = int(input("Valor do primeiro lado:\n "))
l2 = int(input("Valor do segundo lado:\n "))
m = l1*l2
ms = m/3
if m >= 18:
    print("São", ms, "L para area pintada",
          "\n Serão necesarios", ms/18, "galões de tinta para o serviço")
    c = (input("Qual o galão tem preferencia em ultilizar \nA galões de 18 litros por R$80,00:\nTemos galoes por R$25,00 com 3,6 L:\n "))
    if c == 80:
        print("O custo do final do projeto é de:", ((ms/18)*80))
    else:
        print("O custo é de", ((ms/3.6)*25))
else:
    print("Sua metragem é de:",m,"M",
    "\nÉ necessario apenas um galão de tinta")
