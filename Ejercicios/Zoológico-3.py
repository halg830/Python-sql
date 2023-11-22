nombre = input("Digite el nombre del rinoceronte: ")
edad = int(input("Digite la edad del rinoceronte: "))
peso = float(input("Digite el peso en libras: "))
longitud = float(input("Digite la longitud en pies: "))

libra = 0.453592
pie = 0.3048

kg = peso*libra
m = longitud*pie

print("El rinoceronte ", nombre, " con la edad ", edad, "pesa ", kg, "kg y tiene una longitud de ", m)