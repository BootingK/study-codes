print('Calcular dobro de um quadrado perfeito')
baseStr = input('Qual é a medida do lado do quadrado => ');


baseInt = 0;
try:
    baseInt = int(baseStr);
except:
    print('Forneça apenas NÚMEROS');
    
print('O dobro da sua área é',2 * (baseInt ** 2));
