# Criar um programa que leia uma variável nota com input e mostre na tela:
# > 90 "Conceito A"
# entre 89 e 71 "Conceito B"
# entre 70 e 61 "Conceito C"
# entre 60 e 50 "Conceito D"
# < 49 "Conceito E"

nome=(input("Informe seu primeiro nome: "))

série=(input("Informe sua série: "))

n1=int(input("Sua nota no 1° bimestre é "))
n2=int(input("Sua nota no 2° bimestre é "))
n3=int(input("Sua nota no 3° bimestre é "))
n4=int(input("Sua nota no 4° bimestre é "))

n=(n1+n2+n3+n4)/4

if n>=100:
    print(f"Parabéns {nome}, você tirou nota máxima e passou do {série}!")
    print(f"Sua nota final é {n}.")
elif n<100 and n>=80:
    print(f"Você está acima da média e passou do {série}, {nome}!")
    print(f"Sua nota final é {n}.")
elif n<80 and n>=70:
    print(f"Você passou do {série}, {nome}!")
    print(f"Sua nota final é {n}.")
elif n<70 and n>=60:
    print(f"Você passou do {série} por pouco, {nome}!")
    print(f"Sua nota final é {n}.")
else:
    print(f"Você reprovou e ficou no {série}, {nome}.")
    print(f"Sua nota final é {n}.")