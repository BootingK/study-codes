salarioStr = input('Quantos você ganha por hora => ');
horasStr = input('Quantos horas você trabalha por mês => ');

salarioInt = 0;
horasFloat = 0;
try:
    salarioInt = int(salarioStr);
    horasFloat = float(horasStr);
except:
    print('Digite apenas NÚMEROS!!');

rs = float(salarioInt * horasFloat);
print('Seu salário é',rs);
