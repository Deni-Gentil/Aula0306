temperatura=float(input("Digite a temperatura atual: "))
if temperatura>40.1:
    print("Você está com febre.")
elif temperatura<=40.1 and temperatura>=38.9:
    print("Você está com febrícula.")
elif temperatura<=38.8 and temperatura >=37.0:
    print("Temperatura quase ideal.")
elif temperatura<=36.9 and temperatura>=34.9:
    print("Tempertaura normal.")
elif temperatura<=34.8 and temperatura>=32.9:
    print("Pré-hipotermia.")
elif temperatura<=32.8 and temperatura>=29.9:
    print("Hipotermia.")
else:
    print("R.I.P.")