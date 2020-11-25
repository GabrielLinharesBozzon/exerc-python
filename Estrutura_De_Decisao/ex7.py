# -*-coding:utf8-*-
#7)Faça um Programa que leia três números e mostre o maior e o menor deles.
C=0
n=[]
while C<3:
    d=int(input("Digite o numero:\n"))
    n.append(d)
    C+=1
n.sort(reverse=True)
print("O maior deles é",n[0])
print("O menor deles é",n[2])