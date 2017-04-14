tempuraturaStr = input('Qual é a temperatura em Farenheit? ');
tempuraturaInt = 0;
try:
    tempuraturaInt = int(tempuraturaStr);
except:
    print('Apenas NÚMEROS INTEIROS');
    exit(0);

resultado = float((tempuraturaInt-32) / 1.8); # Fórmula do equação
print();
print();
print('==========RESULTADO=========');
print('Tempuratura é {0:.3}°F'.format(resultado));

