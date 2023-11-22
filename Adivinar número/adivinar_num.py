import random

numSecreto = random.randint(0,100)
 
while True:
   numero = input('Adivina el número!: ')
 
   try:
       numero = int(numero)
   except:
       print('Error ese no es un número.')
       continue
 
   if numero != numSecreto:
       if numero > numSecreto:
           print(numero, 'es mayor que el número secreto')
 
       elif numero < numSecreto:
           print(numero, 'es menor que el número secreto')
   else:
       print('Adivinaste el número:', numSecreto)
       break