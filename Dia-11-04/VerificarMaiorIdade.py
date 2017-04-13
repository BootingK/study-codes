import sys;

name = str(input('Qual é o seu nome ? '));
idade = input('Qual é a sua idade ? ');
a = 0;
try:
    a = int(idade);
except:
    print('Digite apenas números');
    sys.exit(1);
if a >= 18:
    print('Olá',name,'você é maior de idade ;)');
else:
    print('Olá',name,'você não é maior de idade.');


    
    
