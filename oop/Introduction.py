# what is oop?
# oop is a programming paradigm based on the concept of "objects",
# which can contain data, in the form of fields
# (often known as attributes or properties), and code,
# in the form of procedures (often known as methods).

# what is a class?
# A class is a blueprint for the object.

# what is an object?
# An object is an instance of a class.

class Introduction:
    x=10 # property or attribute

    def demo(self): # method or behaviour
        print("Hello World")

# instance of a class
obj = Introduction() # creating an object
print(obj.x) # accessing the property
obj.demo() # accessing the method