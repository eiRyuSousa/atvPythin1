valor = float(input("insira o valor: "))
taxa = float(input("insira a taxa: "))
tempo = float(input("insira o tempo: "))

prestação = valor + (valor * (taxa/100) * tempo)

print("o valor da pretação é: ",prestação)
