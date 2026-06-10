#numero = 7

#if numero % 2 == 0
#    print("Par")
#else:
#    print("Ímpar")

idade = int(input("Minha idade é "))

if idade>=100:
    print("Você está morto.")
elif idade<100 and idade>=60:
    print("Você é um idoso.")
elif idade<60 and idade>=18:
    print("Você é um adulto.")
elif idade<18 and idade>=12:
    print("Você é um adolescente.")
elif idade<12 and idade>=3:
    print("Você é uma criança.")
elif idade<3 and idade>=0:
    print("Você é um bebê.")
else:
    print("Você não existe.")