a=int(input('Digite un número: '))
b=int(input('Digite otro número: '))
c=int(input('Digite un último número: '))

if a==b and a==c and b==c:
    print('Los tres números son iguales')
else:
    if a<b and b<c:
        ma=c
        me=a
    elif a<c and c<b:
        ma=b
        me=a
    elif b<a and a<c:
        ma=c
        me=b
    elif b<c and c<a:
        ma=a
        me=b
    elif c<a and a<b:
        ma=b
        me=c
    elif c<b and b<a:
        ma=a
        me=c

print('El mayor es: ',ma,'\nEl menor es: ',me)