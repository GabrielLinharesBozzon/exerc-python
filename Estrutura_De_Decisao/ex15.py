#15)Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se #o mesmo é: equilátero, isósceles ou escaleno.
#Dicas:
#Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
#Triângulo Equilátero: três lados iguais;
#Triângulo Isósceles: quaisquer dois lados iguais;
#Triângulo Escaleno: três lados diferentes;

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

