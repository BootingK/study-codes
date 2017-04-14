num1Str = input('Primeiro número inteiro => ');
num2Str = input('Segundo número inteiro => ');
num3Str = input('Terceiro número real => ');

num1Int = 0;
num2Int = 0;
num3Float = 0.0;

try:
    num1Int = int(num1Str);
    num2Int = int(num2Str);
    num3Float = float(num3Str);
except:
    print('Digite apenas números');

#     o produto do dobro do primeiro com metade do segundo .
print('=======PRIMEIRO=======');
divisao = int((num1Int * 2) / (num2Int / 2));
produto = int((num1Int * 2) % (num2Int / 2));
print('Divisão {0}'.format(divisao));
print('Produto {0}'.format(produto),"\n");
#     a soma do triplo do primeiro com o terceiro.  (num1 * 3) + num3;
print('=======SEGUNDO=======');
rsa = float((num1Int * 3) + num3Float);
print('Resultado {0:.3}'.format(rsa),'\nEquação (num1 * 3) + num3\n');
#     o terceiro elevado ao cubo.
print('=======TERCEIRO=======');
rsb = float(num3Float ** 3);
print('O número 3 ao cubo é {0:.3}'.format(rsb));
print();
#    verificar se a soma do segundo elevado ao cubo somado com o terceiro é par ou impar
print("==========QUARTO======")
rsc = float( (num2Int ** 3) + num3Float);
if rsc % 2 == 0:
    print('O número {0:.3} é par'.format(rsc));
else:
    print('O número {0:.3} é impar'.format(rsc));
   








