import json


with open("users.txt" , "r") as f:
        userlist = json.loads(f.read())

print(userlist)