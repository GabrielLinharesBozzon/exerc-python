# -*-coding:utf8-*-
#6)Faça um Programa que leia três números e mostre o maior deles.
C=0
n=[]
while C<3:
    d=int(input("Digite o numero:\n"))
    n.append(d)
    C+=1
n.sort(reverse=True)
print(n[0])


