#This is the calculator object
class Calculator:

    #This object has two atributtes which are number one and numbert Two
    def __init__(self, numberO, numberTw):
       self.numberO = numberO
       self.numberTw = numberTw

    #Sum function
    def sum(self):
        return self.numberO + self.numberTw
    #Subsctraction function
    def substraction(self):
        return self.numberO - self.numberTw

    #Multiplication function
    def multiplication(self):
        return self.numberO * self.numberTw
    
    #Division Function 
    def division(self):
        if self.numberTw == 0:
            print("No se puede dividir entre cero")
        else:
            return self.numberO / self.numberTw
    #To the power to n fucntion
    def power(self):
        return self.numberO ** self.numberTw 

"""I'm writting this to show the changes"""

if __name__ == "__main__":
    num1 = 12
    num2 = 24
    calculadora  = Calculator(num1, num2)
    #Results
    print("\n Este es el resultado de la suma", calculadora.sum())
    print("\n Este es el resultado de la resta ", calculadora.substraction())
    print("\n Este es el resultado de la multiplicación ", calculadora.multiplication())
    print("\n Este es el resultado de la division ",calculadora.division())
    print("\n Este es el resultado de la potencia ", calculadora.power())

