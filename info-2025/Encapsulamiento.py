class circulo:
    def __init__(self, radio):
        self.radio = radio
        self.__pi = 3.1416
        
    def calcularPerimetro(self):
        return 2 * self.__pi * self.radio
    
    def calcularArea(self):
        return self.__pi * (self.radio ** 2)
    
    def getPi(self):
        return f"El valor de Pi es:{self.__pi}"
    
    def setPi(self, nuevoValorPi):
        if type(nuevoValorPi) == int or type(nuevoValorPi) == float:
            if nuevoValorPi > 0:
                self.__pi = nuevoValorPi
                print(f"El nuevo valor de Pi es: {self.__pi}")
            else:
                print("El valor de Pi debe ser positivo")
        else:
            print("El valor de Pi debe ser un número")

    
    
circulo_uno = circulo(3.5)

print(circulo_uno.calcularArea())
print(circulo_uno.calcularPerimetro())
# print(f"El valor de Pi en la calse es: {circulo_uno.pi}")

# print(circulo_uno.__dict__)
# print(f"El valor de Pi en la clase es: {circulo_uno._circulo__pi}") # Acceso al atributo privado

print(circulo_uno.getPi()) # Acceso al método que retorna el valor de Pi


print(circulo_uno.setPi(3.14159)) # Cambiando el valor de Pi
print(circulo_uno.getPi()) # Verificando el nuevo valor de Pi
print(circulo_uno.setPi(-3)) # Intentando establecer un valor negativo
