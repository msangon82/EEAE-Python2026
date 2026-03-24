class Calculadora:
    def __init__(self, num1,num2):
        self.n1 = num1
        self.n2 = num2
    
    def sumar(self):
        return (self.n1 + self.n2)

if __name__ == "__main__":
    print("Estás ejecutando el archivo de clases, NO EL PROGRAMA PRINCIPAL")
    calc = Calculadora(2,5)
    print(calc.sumar())