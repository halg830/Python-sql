nombre = input("Digite el nombre del empleado: ")
horas = int(input("Digite las horas trabajadas: "))
cuota = float(input("Digite la cuota por hora trabajada: "))

incentivo = 0.05

sueldo=horas*cuota

if horas>40:
    sueldo+=sueldo*incentivo

print("El sueldo del empleado", nombre, "es: ", sueldo)