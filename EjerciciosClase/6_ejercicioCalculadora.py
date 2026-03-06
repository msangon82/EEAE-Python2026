# Crea una clase Calculadora que reciba dos numeros.
# Haz los siguientes métodos:
# - Un método para sumar los dos números
# - Un método para restar los dos números
# - Al hacer print de un objeto Calculadora se impriman los dos números
# Añade try-except para validar la entrada de datos

class Calculadora:
    def __init__(self, num1, num2):
        self.a = num1
        self.b = num2
        self.resultado = None

    def sumar(self):
        try:
            self.resultado = self.a + self.b
        except:
            try:
                self.resultado = int(self.a) + int(self.b)
            except:
                self.resultado = "No son numeros los datos introducidos"
        return self.resultado
            

    def restar(self):
        return (self.a - self.b)
    
    def __str__(self):
        return (f"Los números son {self.a} y {self.b}")

calc1 = Calculadora("melocotones", 2)
print(calc1.sumar())
