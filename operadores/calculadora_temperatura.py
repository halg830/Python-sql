cantidad=float(input('Digite la cantidad a convertir: '))
tempI=input('Digite la temperatura en la que esta: \n c: celsius \n f: fahrenheit \n k: kelvin \n')
tempF=input('Digite la temperatura a la que desea convertir: \n c: celsius \n f: fahrenheit \n k: kelvin \n')

if tempI=="c" and tempF=="f":
    f=cantidad*1.8+32
elif tempI=="c" and tempF=="k":
    k=cantidad+273.15
elif tempI=="f" and tempF=="c":
    c=(cantidad-32)/1.8
elif tempI=="f" and tempF=="k":
    k=(cantidad+459.67)/1.8
elif tempI=="k" and tempF=="c":
    c=cantidad-273.15
elif tempI=="k" and tempF=="f":
    f=(cantidad-273.15)*9/5+32 

if tempF=="c":
    print('La temperatura en ',tempF," es: ",c,"°C")
elif tempF=="f":
    print('La temperatura en ',tempF," es: ",f,"°F")
elif tempF=="k":
    print('La temperatura en ',tempF," es: ",k,"°K")
