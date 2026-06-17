#Descobrindo o tamanho da lista
nomes = ["Deni", "Lucas", "Leander", "Landus", "Paulo", "Bianca"]

print(len(nomes))

#Saber se existe um elemento na lista
if "Wilson" in nomes:
    print("Está na lista")
else:
    print("Não está na lista")

#A posição de um elemento na lista
indice = nomes.index("Bianca")
print(f"A Bianca está no indíce {indice}")

#Percorrer a lista
for nome in nomes:
    print(nome)

#Percorrer a lista com índice e valor
for name, nome in enumerate(nomes):
    print(name, nome)

#Limpar toda a lista
nomes.clear()
print(nomes)

nomes.append("Wilson")
print(nomes)