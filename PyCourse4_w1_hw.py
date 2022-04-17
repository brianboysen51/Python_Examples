#q1 - 

class Bike:
    def __init__(self,color,price):
        self.color=color
        self.price=price

testOne=Bike("blue",89.99)
testTwo=Bike("purple",25.0)

#q2 - 
class AppleBasket:
    def __init__(self,color,quant):
        self.apple_color=color
        self.apple_quantity=quant
        
    def increase(self):
        self.apple_quantity+=1
        return self.apple_quantity
    
    def __str__(self):
        return "A basket of {} {} apples.".format(self.apple_quantity,self.apple_color)

val1=AppleBasket('red',8)
print(val1)
print(val1.increase())

#q3 - 

class BankAccount:
    def __init__(self,name,amt):
        self.name=name
        self.amt=amt
        
    def __str__(self):
        return "Your account, {}, has {} dollars.".format(self.name,self.amt)
    
t1=BankAccount("Bob",100)
print(t1)