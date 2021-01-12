# -*- coding: latin-1 -*-
'''Verificando o tipo de triangulo:
Programa verifica se o triangulo é equilatero, isosceles ou escaleno, caso nao seja nenhum printa ~
não pode ser um triangulo
'''

lado1 = input('Digite o primeiro: ')
lado2 = input('Digite o segundo lado: ')
lado3 = input('Digite o terceiro lado: ')

if lado1 + lado2 > lado3:
    if lado1 == lado2 and lado1 == lado3:
        print ('E um Triangulo equilatero')
    elif lado1 == lado2 or lado2 == lado3 or lado1 == lado3:
        print ('E um Triangulo isosceles')
    elif lado1 != lado2 and lado3 or lado2 != lado1 and lado3 or lado1 != lado3:
        print ('E um Triangulo escaleno')

else:
    print ('Os valores informados não formam um Triangulo')