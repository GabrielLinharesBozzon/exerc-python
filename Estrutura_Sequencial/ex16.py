#16)Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).
mb=float(input("Escreva o tamanho do arquivo:\n"))
mbps=float(input("Qual velocidade da Internet:\n "))
vc=((mb*mbps)/60)
print("O seu tempo é de ",vc,"M")