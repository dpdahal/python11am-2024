# what is module?
# module is a file containing python code.
# A module can define functions,
# classes and variables. A module can also include runnable code.

# types of modules
# 1. built-in modules: datetime, math, random, sys, os, etc.
# 2. user-defined modules: created by user.

# import datetime
# post_date ="2020-01-01"
# post_date = datetime.datetime.strptime(post_date, "%Y-%m-%d")
# print(post_date)
# today = datetime.date.today()
# birthday = datetime.date(1995, 1, 1)
# print(today-birthday)


jobs =[
    {'title':"python developer","exp_date":"2020-01-01"},
    {'title':"java developer","exp_date":"2024-01-01"},
    {'title':"php developer","exp_date":"2022-01-01"},
    {'title':"c++ developer","exp_date":"2021-01-01"},
    {'title':"c# developer","exp_date":"2024-06-08"},
]

# import datetime

# for job in jobs:
#     exp_date = job['exp_date']
#     job_date = datetime.datetime.strptime(exp_date, "%Y-%m-%d")
#     today = datetime.datetime.today()
#     if job_date < today:
#         print(f"{job['title']} is expired")
#     else:
#         print(f"{job['title']} is not expired")
   
import sys 
import os
import glob