#15)Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se #o mesmo é: equilátero, isósceles ou escaleno.
#Dicas:
#Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
#Triângulo Equilátero: três lados iguais;
#Triângulo Isósceles: quaisquer dois lados iguais;
#Triângulo Escaleno: três lados diferentes;

L1=int(input("Digite o primeiro lado:\n"))
L2=int(input("Digite o segundo  lado:\n"))
L3=int(input("Digite o terciero lado:\n"))

if L1==L2:
    if L2==L3:
        if L3==L1:
         print("Triângulo Equilátero")

if(L1>=L2)or(L1<=L2):
    if(L2>=L3)or(L2<=L3):
        if(L3>=L1)or(L3<=L1):
            print("Triângulo Escaleno")

