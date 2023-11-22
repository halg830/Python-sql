nombre=input('Digite su nombre: ')
peso=float(input('Digite su peso en kg: '))
estatura=float(input('Digite su estatura en metro: '))

imc=peso/estatura**2

if imc>=18.5 and imc<=24.9:
    print(nombre, 'tiene el imc en normal')
elif imc>=25 and imc<=29.9:
    print(nombre, 'tiene el imc en sobrepeso')
elif imc>=30 and imc<=34.9:
    print(nombre, 'tiene el imc en obesidad grado I')
elif imc>=35 and imc<=39.9:
    print(nombre, 'tiene el imc en obesidad grado II')
elif imc>=40:
    print(nombre, 'tiene el imc en obesidad grado III')