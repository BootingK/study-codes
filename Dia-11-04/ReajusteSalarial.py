salarioStr = input('Informe seu salário => ');

salarioInt = 0;
try:
    salarioInt = int(salarioStr);
except:
    print('Digite apenas NÚMEROS');
    
if salarioInt <= 1700:
    print('Seu salário sofreu um reajuste de + %10 por ser maior de 1700,passando para',salarioInt + (salarioInt * 0.10));
else:
    print('Seu salário sofreu um reajuste de - %5 por ser maior de 1700,passando para',salarioInt - (salarioInt * 0.05))



