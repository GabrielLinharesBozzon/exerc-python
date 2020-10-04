# Faça um Programa que peça as 4 notas bimestrais e mostre a média.
c = int(0)
nota = []
while c < 4:
    nota.append(int(input("Digite a nota:")))
    c += 1
x = (sum(nota)/4)
nota.sort()
print("As notas são ", nota, "\n","Sua média foi", x)
