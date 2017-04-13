import sys;

nota1str = input('Nota do primeiro bimestre: ');
nota2str = input('Nota do segundo bimestre: ');
nota3str = input('Nota do terceiro bimestre: ');
nota4str = input('Nota do quarto bimestre: ');

nota1Integer = 0;
nota2Integer = 0;
nota3Integer = 0;
nota4Integer = 0;
try:
    nota1Integer = int(nota1str);
    nota2Integer = int(nota2str);
    nota3Integer = int(nota3str);
    nota4Integer = int(nota4str);
except:
    print('Digite apenas NÚMEROS');
    sys.exit(0);
if nota1Integer > 10:
    print('Sua nota não pode ser maior que 10');
    sys.exit(0);
elif nota2Integer > 10:
    print('Sua nota não pode ser maior que 10');
    sys.exit(0);
elif nota3Integer > 10:
    print('Sua nota não pode ser maior que 10');
    sys.exit(0);
elif nota4Integer > 10:
    print('Sua nota não pode ser maior que 10');
    sys.exit(0);
rs = int((nota1Integer + nota2Integer + nota3Integer + nota4Integer) / 4);   
print('Sua nota final é',rs);
print('');
print('=====CLASSIFICAÇÃO===');
if rs < 5:
    print('Você não tirou nota o suficiente para passar de ano');
elif rs >= 5:
    print('Você tirou nota o suficiente para passar de ano.Parabéns !!');
print('=====CLASSIFICAÇÃO===');
