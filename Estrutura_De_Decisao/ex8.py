# -*-coding:utf8-*-
#8)Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.
C=int(0)
n=[]
while C<3:
    C+=1
    n.append(float(input("Digite o preço:\n")))
n.sort(reverse=True)
print("O maior deles é",n[0])
print("O menor deles é",n[2])