# Ejercicio 1: Calculadora básica con clases 
# Crea una clase Calculadora que tenga métodos para sumar, restar, multiplicar y dividir dos números. 
# Incluye un constructor que inicialice los dos números como atributos.
class Calculadora:

    def __init__(self,a,b):
       self.num1 = a
       self.num2 = b
    
    def suma(self):
        return (f"{self.num1} + {self.num2} = {self.num1 + self.num2}")

    def resta(self):
        return(f"{self.num1} - {self.num2} = {self.num1 - self.num2}")
    
    def producto(self):
        return(f"{self.num1} * {self.num2} = {self.num1 * self.num2}")
    
    def division(self):
        return(f"{self.num1} / {self.num2} = {self.num1 / self.num2}")
    
    def raiz(self):
        return(f"Raíz{self.num2} de {self.num1} = {round(self.num1**(1/self.num2),2)}")

    def __str__(self):
        return(f"Números: {self.num1} y {self.num2}")

c4y5 = Calculadora(4,5)

print(c4y5)
print(c4y5.suma())
print(c4y5.resta())
print(c4y5.producto())
print(c4y5.division())
print(c4y5.raiz())