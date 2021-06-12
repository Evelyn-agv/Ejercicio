class Asignacion:
    c=0
    
    def __init__(self):
        self.num1= int(input("Ingrese el primer numero: "))
        self.num2= int(input("Ingrese el segundo numero: "))
        self.num3= int(input("Ingrese el tercer numero: "))
    
    def respuesta(self):
        # condiciones
        if self.num1 == self.num2:
            print("El numero 1: {}, el numero 2: {} son iguales" .format(self.num1, self.num2))
        elif self.num1 == self.num3:
            print("El numero 1: {}, el numero 3: {} son iguales" .format(self.num1, self.num3))
        elif self.num2 == self.num3:
            print("El numero 2: {}, el numero 3: {} son iguales" .format(self.num2, self.num3))
        else: 
            print("Los numeros no son iguales")



if __name__ == '__main__':
    #usar clase
    asig= Asignacion() 
    asig.respuesta()  #Llamar metodo de la clase
    print(asig.num1)  #Llamar atributo de la clase
    print(asig.num2)
    print(asig.num3)
