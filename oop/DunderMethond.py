# class Employee:
#     def __new__(cls):
#         print("This is new method")
#         return object.__new__(cls)

#     def __init__(self):
#         print("This is constructor")

#     def emp_name(self):
#         print("This is emp_name method")

#     def __del__(self):
#         print("This is destructor")

   

# obj = Employee()
# # obj.emp_name()


# class Student:
#     def __init__(self,id,name):
#         self.student_id=id
#         self.student_name=name
#         # print(f"Id is {id} and name is {name}")



# obj = Student(101,"sophia")
# print(obj.student_id)
# print(obj.student_name)


# class Student:
#     total=0
#     def __init__(self,name):
#         Student.total+=1
    

# obj1 = Student("sophia")
# obj2 = Student("hari")
# obj3 = Student("gita")
# obj4 = Student("sita")
# print(obj1)


class Student:

    def __init__(self):
        self.name ='hari'
        self.age = 20
        self.address = 'ktm'

    def __str__(self):
        return self.name
    

obj1 = Student()
print(obj1)