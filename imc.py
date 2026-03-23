# Programa para calcular o IMC e mostrar a classificação

# Entrada
peso = float(input("Digite seu peso (kg): "))
altura = float(input("Digite sua altura (m): "))

# Cálculo do IMC
imc = peso / (altura * altura)

# Processamento
if imc < 16:
    classificacao = "Magreza grave"
elif imc < 17:
    classificacao = "Magreza moderada"
elif imc < 18.5:
    classificacao = "Magreza leve"
elif imc < 25:
    classificacao = "Saudável"
elif imc < 30:
    classificacao = "Sobrepeso"
elif imc < 35:
    classificacao = "Obesidade Grau I"
elif imc < 40:
    classificacao = "Obesidade Grau II (severa)"
else:
    classificacao = "Obesidade Grau III (mórbida)"

# Saída
print(f"IMC: {imc:.2f}")
print(f"Classificação: {classificacao}")