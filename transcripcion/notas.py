nota=float(input('El resultado de la nota es:\n'))

if nota>=4.5 and nota <= 5.0:
    print('Sobresaliente', str(nota))
elif nota >=4.2 and nota <=4.4:
    print("Notable",str(nota))
elif nota >=3.8 and nota <=4.1:
    print("Suficiente", str(nota))
elif nota >=0.0 and nota <=2.9:
    print("Insuficiente",str(nota))
else:
    print('Error:Puntuación incorrecta',str(nota))