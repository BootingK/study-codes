a = int(input('Número 1: '));
b = int(input('Número 2: '));
c = int(input('Número 3: '));
check1 = bool(False);
if a > b:
    check1 = bool(True);
    
if check1:
   if a > c:
       print('O número',a,'é o maior');
   elif a < c:
       print('O número',c,'é o maior');
else:
   if b > c:
       print('O número',b,'é o maior');
   elif b < c:
       print('O número',c,'é o maior');
