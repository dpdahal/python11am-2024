# what is inheritance?
# Inheritance is parent-child relationship between classes

# class Laptop:
#     def brand(self,name):
#         return f"Brand name is {name}"
    
#     def product_size(self,size):
#         return f"Product size is {size}"


# class Dell(Laptop):
    
#     def price(self,price):
#         return f"Price is {price}"

# class HP(Laptop):
#     pass

# obj = Dell()
# print(obj.brand("Dell"))
# print(obj.price(20000))


class A:
    def info(self):
        return "This is class A"

class B(A):
    def test(self):
        return "This is class B"


class C(B):
    pass

obj = C()
print(obj.info())
print(obj.test())