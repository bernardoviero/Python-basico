import random

dicionario = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"];
numeros_placa = [];
letras_placa = [];
placas = [];

qtdPlacas = int(input("Digite a quantidade de placas desejadas: "));

for quantidade in range(qtdPlacas):
    letras = "";
    numeros = "";
    placa = "";
    for _ in range(3):
        letras += random.choice(dicionario);
    numero_aleatorio = random.randint(1, 9);
    numeros += str(numero_aleatorio);
    placa += letras + numeros;
    letras = "";
    letras += random.choice(dicionario);
    placa += letras;        
    for _ in range(1):
        numeros += str(numero_aleatorio);
    placa += numeros;
    placas.append(placa);

for placa in placas:
    print("PLACAS:", placa);