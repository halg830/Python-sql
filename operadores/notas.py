print('Ingrese su puntuación entre (0.0 a 5.0)')

puntaje = float(input())

if puntaje < 0 or puntaje > 5.0:
    print('La puntuación esta fuera del rango permitido')
elif puntaje >= 0 and puntaje <= 2.9:
    print('Insuficiente')
elif puntaje >= 3.0 and puntaje <= 3.7:
    print('Suficiente')
elif puntaje >= 3.8 and puntaje <= 4.1:
    print('Bien')
elif puntaje >= 4.2 and puntaje <= 4.4:
    print('Notable')
elif puntaje >= 4.5 and puntaje <= 5.0:
    print('Sobresaliente')
else:
    print('Puntuación incorrecta')