class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b
    
    def multiply(self, a, b):
        return a * b
    
obj = Calculator()
print(obj.add(10, 20))
print(obj.subtract(10, 20))
print(obj.multiply(10, 20))