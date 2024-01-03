# what is constructor?
# constructor is a special method in python which is used to 
# initialize the instance members of the class.

# class Student:

#     def __init__(self):
#         print("This is constructor")

#     def test(self):
#         print("This is test method")

#     def __del__(self):
#         print("This is destructor")

# obj = Student()
# obj.test()


class Employee:
    def __str__(self):
        return "Employee class"


obj = Employee()
print(obj)