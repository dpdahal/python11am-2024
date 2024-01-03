# types of loop
# 1. for loop: list, tuple, set, dictionary, string
# 2. while loop: condition
# 3. nested loop: loop inside loop

# while loop

# x=1

# while x<=10:
#     print(x,"Ram")
#     x+=1


# x=10

# while x>=1:
#     print(x,end=" ")
#     x-=1

# num=1
# fix_value=5

# while num<=10:
#     print(fix_value,"x",num,"=",fix_value*num)
#     num+=1

# total_num=0
# total_even=0
# total_odd=0

# x=1
# while x<=10:
#     total_num=total_num+x
#     if x%2==0:
#         total_even+=1
#     else:
#         total_odd+=1
#     x+=1

# print("total_num",total_num)
# print("total_even",total_even)
# print("total_odd",total_odd)

# name = input("Enter your name: ")
# x=1
# while x<=10:
#     print(name)
#     x+=1

numbers=[23,56,76,57,86,13,11,21,21]
x=0
while x<len(numbers):
    print(numbers[x])
    x+=1