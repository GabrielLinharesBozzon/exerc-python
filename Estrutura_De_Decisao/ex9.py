#-*-coding:utf8-*-
# 9)Faça um Programa que leia três números e mostre-os em ordem decrescente.
C=int(0)
n=[]
while C<3:
    C+=1
    n.append(float(input("Digite o preço:\n")))
n.sort(reverse=True)
print(n)
