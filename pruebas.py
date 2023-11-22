#Apropiación 1

#1
""" cantFrutosRecoletados = int(input("Ingrese la cantidad de frutos recoletados: "))
cantFrutosProducidos = int(input("Ingrese la cantidad de frutos producidos: "))

indiceCosecha = (cantFrutosRecoletados/cantFrutosProducidos)*100

print(indiceCosecha) """

#2
""" print("+---+\n|   |\n|   |\n+---+\n|\n|\n") """

#3


nivelHemoglobina = float(input("Ingrese su nivel de hemoglobina en la sangre: "))
edad = input("¿Su edad esta en meses o años?\n m:meses \n a:años")
if edad=="m": mes = int(input("Ingrese sus meses: "))
elif edad=="a": año = int(input("Ingrese sus años: "))
sexo = input("Ingrese su sexo: \n m:mujeres \n h:hombres")

if edad=="m":
    if mes>=0 and mes<=1: 
        if nivelHemoglobina<13 and nivelHemoglobina>26: resultado="negativo"
        else: resultado="positivo"
    elif mes>1 and mes<=6: 
        if nivelHemoglobina<10 and nivelHemoglobina>18: resultado="negativo"
        else: resultado="positivo"
    elif mes>6 and mes<=12: 
        if nivelHemoglobina<11 and nivelHemoglobina>15: resultado="negativo"
        else: resultado="positivo"

if edad=="a":
    if año>1 and año<=5: 
      if nivelHemoglobina<11.5 and nivelHemoglobina>15: resultado="negativo"
      else: resultado="positivo"
    elif año>5 and año<=10: 
      if nivelHemoglobina<12.6 and nivelHemoglobina>15.5: resultado="negativo"
      else: resultado="positivo" 
    elif año>10 and año<=15:
      if nivelHemoglobina<13 and nivelHemoglobina>15.5: resultado="negativo"
      else: resultado="positivo"
    elif sexo=="m" and edad>15:
      if nivelHemoglobina<12 and nivelHemoglobina>16: resultado="negativo"
      else: resultado="positivo"
    elif sexo=="h" and año>15:
      if nivelHemoglobina<14 and nivelHemoglobina>18: resultado="negativo"
      else: resultado="positivo"

print(f"Su resultado es: {resultado}")