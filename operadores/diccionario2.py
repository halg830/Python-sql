nombre = input('¿Cómo te llamas?')
edad = input('Cuántos años tiene?')
telefono = input('¿Cuál es tu número de teléono?')
cuidadResidencia = input('¿Ciudad de residencia?')
empresa = input('¿Empresa donde traba?')
sueldo = input('¿Sueldo que gana?')

persona = {'nombre': nombre, 'edad': edad, 'telefono': telefono,
           'cuidadResidencia': cuidadResidencia,
           'empresa':empresa, 'sueldo': sueldo}

print(persona[ 'nombre'], 'tiene', persona[ 'edad'], 'años, vive en',
      persona['cuidadResidencia'], 'su número de', persona['telefono'],
      'trabaja en', persona['empresa'], 'y devenga un sueldo de', persona['sueldo'])