# operators
# 1. Arithmetic Operators: +, -, *, /, %, **, //
# print(10%3)
# print(2**4)

# print(19//5)

# a = (4+7)/3*2


# 2. Assignment Operators: =, +=, -=, *=, /=, %=, **=, //=

# a=5
# a=10
# print(a)


# 3. Comparison Operators: ==, !=, >, <, >=, <=

# print(5==6)
# print(6>7)
# print(6<8)

# print(a=7)

# 4. Logical Operators: and, or, not

# if else elif

# 5. Identity Operators: is, is not
# 6. Membership Operators: in, not in

# a =5
# b=6
# c=a
# print(id(a))
# print(id(b))
# print(id(c))
# print(a is b)
# print(a is c)
# print(a is not b)
# print(a is not c)


# name ='ram'
# print('r' in name)
# print('x' in name)

# 7. Bitwise Operators: &, |, ^, ~, <<, >>

# print(5&6)
# print(bin(5))
# print(bin(6))

# 101
# 110
# 100
# print(bin(4))

# a = 50
# b = 7
# if a>b:
#     print("a is greater then b")
# else:
#     print("b is greater then a")

# WAP to enter any number and check whether it is even or odd
# WAP to enter any number and check whether 
# it is divisible by 3 and 5

# WAP to enter five subject makrs
#  and find total and percentage grade
# 35-45 D
# 45-60 C
# 60-80 B
# 80-100 A

# nep = int(input("Enter nepali marks: "))
# eng = int(input("Enter english marks: "))
# mat = int(input("Enter math marks: "))
# sci = int(input("Enter science marks: "))
# com = int(input("Enter computer marks: "))
# total = nep+eng+mat+sci+com
# per = total/5
# print("Total: ",total)
# print("Percentage: ",per)
# if per>35 and per<45:
#     print("Grad: D")
# elif per>45 and per<60:
#     print("Grad: C")
# elif per>60 and per<80:
#     print("Grad: B")
# elif per>80 and per<100:
#     print("Grad: A")
# else:
#     print("Fail")

# a =5
# b=68
# c=7

# if a>b and a>c:
#     print("a is greater")
# elif b>a and b>c:
#     print("b is greater")
# else:
    # print("c is greater")

# username = input("Enter username: ")


# if username=='admin':
#     password = input("Enter password: ")
#     if password=='admin002':
#         print("Welcome to admin panel")
#     else:
#         print("Invalid password")
# else:
#     print("Invalid username")

# if username =='admin' and password=='admin002':
#     print("Welcome to admin panel")
# else:
#     print("Invalid username or password")

print("============ATM============")
pin =int(input("Enter your pin: "))
if pin==1234:
    print("1. Withdraw 2. Balance check")
    option = int(input("Enter your option: "))
    amount=10000
    if option==1:
        am = int(input("Enter amount: "))
        if am>amount:
            print("Insufficient balance")
        else:
            rem = amount-am
            print("Withdraw amount: ",am)
            print("Your balance is: ",rem)
    else:
        print("Your balance is: ",amount)
else:
    print("Invalid pin")