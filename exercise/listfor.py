# data =['ram','sita','gita']

# for name in data:
#     print(name)

# users =[
#     ['ram','sita','gita'],
#     ['hari','laxmi','gopal'],
#     ['madan','kabita','binita']
# ]
# for names in users:
#     for name in names:
#         print(name)

# numbers=[
#     [12,34,56,76,56],
#     [34,56,78,98,45],
#     [23,45,67,89,90]
# ]

# fTotal=0
# lTotal=0
# newList=[]
# for number in numbers:
#     fTotal+=number[0]
#     lTotal+=number[-1]

# new_list =[fTotal,lTotal]
# print(new_list)

# num =[11,12,13,14,11,12,14,45]
# new_item = set(num)
# print(new_item)

# new_list=[]
# for n in num:
#     if not n in new_list:
#         new_list.append(n)

# print(new_list)

# users=[
#     {"username":"ram","password":"ram002"},
#     {"username":"admin","password":"admin002"},
#     {"username":"sita","password":"sita002"},
# # ]
# username=input("Enter username:")
# password=input("Enter password:")
# is_login=False
# for user in users:
#     uname =user['username']
#     upass =user['password']
#     if username == uname and password == upass:
#         is_login=True
    
# if is_login:
#     print("Welcome",username)
# else:
#     print("Invalid username or password")


# users=[
#     {"name":"ram","gender":"male","status":True},
#     {"name":"hari","gender":"male","status":False},
#     {"name":"sita","gender":"female","status":True},
#     {"name":"gita","gender":"female","status":False},
#     {"name":"gopal","gender":"male","status":True},
# ]

# total_user=len(users)
# total_male=0
# total_female=0
# total_active_user=0
# total_inactive_user=0
# total_active_male=0
# total_inactive_male=0
# total_active_female=0
# total_inactive_female=0

# for user in users:
#     if user['gender']=='male':
#         total_male+=1
#         if user['status']==True:
#             total_active_male+=1
#         else:
#             total_inactive_male+=1
#     else:
#         total_female+=1
#         if user['status']==True:
#             total_active_female+=1
#         else:
#             total_inactive_female+=1

#     if user['status']==True:
#         total_active_user+=1
#     else:
#         total_inactive_user+=1

# print("Total user:",total_user)
# print("Total active user:",total_active_user)
# print("Total inactive user:",total_inactive_user)


# course=[
#     {"title":"python","price":"20000"},
#     {"title":"java","price":"18000"},
#     {"title":"php","price":"15000"},
# ]

# name = input("Enter course name:")
# is_found=False
# course_details="";
# for cs in course:
#     if name == cs['title']:
#         course_details=cs["title"]+" "+ cs["price"]
#         is_found=True
        

# if is_found:
#     print(course_details)
# else:
#     print("Course not found " + name)


a =10
b=20

temp=a
a=b
print(a)