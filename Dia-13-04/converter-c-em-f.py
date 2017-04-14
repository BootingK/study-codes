temperaturaStr = input('Qual é a temperatura em Celsius? => ');
temperaturaInt = 0.0;
try:
    temperaturaInt = float(temperaturaStr);
except:
    print('Apenas números reais');
    exit();
print();
print();
print('==============RESULTADO==========');
print('O resultado é {0:.3}°F'.format((temperaturaInt * 1.8) + 32));    
