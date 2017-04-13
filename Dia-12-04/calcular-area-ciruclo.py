import math;

raiostr = input('Forneca o raio do círculo => ');

raioFloat = 0.0;
try:
    raioFloat = float(raiostr);
except:
    print('Forneça apenas número decimais');

areafloat = float(math.pi * (raioFloat ** 2));   
print('A área é',areafloat);
