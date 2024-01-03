# import json

# # Dictionary

# data={
#     'name':'ram',
#     'age':20,
#     'address':'ktm'
# }
# # print(data)

# # convert dictionary to json
# jsondata=json.dumps(data)
# # print(jsondata)

# # convert json to dictionary
# data=json.loads(jsondata)
# # print(data)

# # write json data to file
# # with open('jsondata/data.json','w') as file:
# #     json.dump(data,file)

# # read json data from file
# with open('jsondata/data.json','r') as file:
#     saveData=json.load(file)
#     print(saveData)

import requests


data = requests.get("https://jsonplaceholder.typicode.com/users")
data = data.json()


