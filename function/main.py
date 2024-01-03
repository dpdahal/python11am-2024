# what is function?
# function is a block of code which only runs when it is called.
# types of function:
# 1. built in function: print(), input(), len(), etc.
# 2. user defined function: def function_name():

# def greet():
#     print("Hello, world!")

# greet()

# function with parameter

# def user_message(name):
#     print(f"Hello, {name}")

# user_message('Rahul')
# user_message('Raj')

# WAP to make total function which takes 
# two parameter and calculate the total of them.

# def total(x,y):
#     print(x+y)

# total(10,20)

# function with default parameter

# def user(name,age=0):
#     print(name)
#     print(age)

# user('Rahul',30)

# def oneToTen():
#     x=1
#     while x<=10:
#         print("Hello, world!")
#         x+=1

# oneToTen()

# *args and **kwargs
# *args: it is used to pass the variable
#    number of arguments to a function.
# **kwargs: it is used to pass the variable
#    number of keyword arguments to a function.

# def numbers(*args,**kwargs):
#     print(args)
#     print(kwargs)
    
# numbers(10,56,7,89,90,name='ram',age=20)


# function return value

# def total():
#    return [200,45,65]

# print(total())
# What is lambda function?
# lambda function is a small anonymous function.
# total = lambda x,y:x+y
# print(total(10,20))

# function scope: local and global

# x=10


# def test():
#     a=50
#     print(x)
#     print(a)

# test()

# a=50

# def test():
#     global a
#     a=a+40
#     print(a)


# test()
# print(a)


# def take_value():
#     p=5000
#     r=10
#     t=2
#     return [p,r,t]


# def calculate():
#     p,t,r = take_value()
#     return p*r*t/100
# print(calculate())

# factorial number: 5! = 5*4*3*2*1 = 120

# def fac(n):
#     if n<=1:
#         return 1
#     else:
#         return n*fac(n-1)

# print(fac(5))
#  5-1 = 5*4 =20
# 4-1 =3 * 20 = 60
# 3-1 = 2 * 60 = 120
# 2-1 = 1 * 120 = 120

# nested function: function inside function

# def demo():
#     return "Hello world!"


# a = demo
# print(a())

# def total(x,y):
#     return x+y


# def myTotal(x,y,callback):
#     print(callback(x,y))

# a =int(input("Enter first number: "))
# b = int(input("Enter second number: "))

# myTotal(a,b,total)


# def outer():
#     def inner():
#         print("Hello, world!")

#     return inner
# result=outer()
# result()