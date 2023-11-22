class Cookie:

    # Constructor
    def __init__(self, nombre, forma, chips='Chocolate'):
        # Instance attributes
        self.nombre = nombre
        self.forma = forma
        self.chips = chips

    # Metodo
    def hornear(self):
        #La f es para hacer un salto de línea
        print(f'Esta {self.nombre}, se está horneando con la forma de {self.forma} y pepitas de {self.chips}')
        print('¡¡Disfruta de tu galleta!!')

galleta1= Cookie('galleta magica', 'estrella')
print(id(galleta1))
print(type(galleta1))

print(isinstance(galleta1, Cookie))
# True
print(isinstance(galleta1, int))
# False
print(isinstance('un string', Cookie))
# False

galleta2 = Cookie('galleta blanco y negro', 'cuadrada')
print(galleta2.nombre)

galleta3=Cookie('galleta de colores', 'arbol')
galleta3.hornear()



class Alumno():
    def __init__(self,nombre=""):
        self.nombre=nombre
        self.__secreto="asdasd123"

a1=Alumno("Maria")
print(a1.__secreto)