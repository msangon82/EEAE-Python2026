# Haz una clase Dado que simule el lanzamiento de un dado de 2 caras (moneda)
# Modificalo para introducir el numero de caras al instanciar la clase

import random

class Dado:
    def __init__ (self, caras):
        self.caras = caras
    
    def __str__ (self):
        return str(self.lanzar())
    
    def lanzar(self):
        resultado = random.randint(1, self.caras)
        return resultado

moneda = Dado(2)
d6 = Dado(6)
d8 = Dado(8)
d10 = Dado(10)
d12 = Dado(12)
d20 = Dado(20)

dadoRaro = Dado(random.randint(1, 6))

print(f"Tu dado de mierda tiene {dadoRaro.caras} caras y salió un {dadoRaro}")

