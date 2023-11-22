import random


# Variables globales
palabras = []
intentos_permitidos = 6

# Función para agregar una palabra a la lista de palabras
def agregar_palabra():
    palabra = input("Ingrese una palabra para agregar al juego: ").lower()
    palabras.append(palabra)
    print(f'La palabra "{palabra}" se ha agregado al juego.')

# Función para configurar el número de intentos permitidos
def configurar_intentos():
    global intentos_permitidos
    try:
        intentos_permitidos = int(input("Ingrese el número de intentos permitidos: "))
        print(f'Se han configurado {intentos_permitidos} intentos permitidos.')
    except ValueError: 
        print("Por favor, ingrese un número válido.")

# Función para seleccionar una palabra aleatoria de la lista de palabras
def seleccionar_palabra():
    return random.choice(palabras)

# Función para jugar al ahorcado
def jugar():
    palabra = seleccionar_palabra()
    palabra_oculta = ['_'] * len(palabra)
    letras_ingresadas = []
    intentos_restantes = intentos_permitidos

    print("¡Bienvenido al juego del ahorcado!")
    print(f"Tienes {intentos_permitidos} intentos para adivinar la palabra.")

    while intentos_restantes > 0 and '_' in palabra_oculta:
        print("Palabra: " + " ".join(palabra_oculta))
        print("Letras ingresadas: " + " ".join(letras_ingresadas))
        letra = input("Ingrese una letra: ").lower()

        if len(letra) == 1 and letra.isalpha():
            if letra in letras_ingresadas:
                print("Ya has adivinado esa letra antes.")
            elif letra in palabra:
                for i in range(len(palabra)):
                    if palabra[i] == letra:
                        palabra_oculta[i] = letra
                letras_ingresadas.append(letra)
            else:
                letras_ingresadas.append(letra)
                intentos_restantes -= 1
                print(f"La letra '{letra}' no está en la palabra. Te quedan {intentos_restantes} intentos.")

    if '_' not in palabra_oculta:
        print("¡Felicidades! Has adivinado la palabra: " + palabra)
    else:
        print("¡Perdiste! La palabra era: " + palabra)
        print('''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========''')

# Menú principal
while True:
    print("\nMenú:")
    print("1. Agregar Palabra")
    print("2. Configurar")
    print("3. Jugar")
    print("4. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == '1':
        agregar_palabra()
    elif opcion == '2':
        configurar_intentos()
    elif opcion == '3':
        if not palabras:
            print("Agrega palabras al juego primero.")
        else:
            jugar()
    elif opcion == '4':
        break
    else:
        print("Opción no válida. Inténtalo de nuevo.")
