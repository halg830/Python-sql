import math
class punto():
    def __init__(self, x=0,y=0):
        self.x=x
        self.y=y
   
    def mostrar(self):
        return str(self.x)+":"+str(self.y)
   
    def distancia(self, otro):
        dx = self.x - otro.x
        dy = self.y - otro.y
        return math.sqrt((dx*dx + dy*dy))
    
class punto3d(punto):
    def __init__(self,x=0,y=0,z=0):
        super().__init__(x,y)
        self.z=z

    @property
    def z(self):
        print("Doy z")
        return self.__z

    @z.setter
    def z(self,z):
        print("Cambio z")
        self.__z=z

    def mostrar(self):
       return super().mostrar()+":"+str(self.__z)

    def distancia(self,otro):
        dx = self.x - otro.x
        dy = self.y - otro.y
        dz = self.__z - otro.__z
        return (dx*dx + dy*dy + dz*dz)**0.5
    
punto1=punto()
punto2=punto(4,5)
print(punto1.distancia(punto2))

punto3 = punto3d(1,2,3)
print(punto3.distancia(punto3d(2,3,4)))