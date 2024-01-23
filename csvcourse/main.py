# # with open("csvcourse/students.csv") as file:
# #     for data in file:
# #         print(data)
    
# import csv

# # print(dir(csv))

# with open("csvcourse/students.csv","a") as file:
#     # reader = csv.reader(file)
#     # reader = csv.DictReader(file)
#     # for data in reader:
#     #     print(data)

#     writer = csv.writer(file)
#     writer.writerow(["s_n","name","email","address"])
#     writer.writerow([1,"sujit","sujit@gmail.com","ktm"])

    

import numpy as np


data =[1,2,3,4,5,6,7,8,9,10]
data1 =[20,30,40,50,60,70,80,90,100,110]

first_array = np.array(data)
secondd_array = np.array(data1)
all = first_array + secondd_array
print(all)