import json
import random


json_content = open("./src/user.json").read()
user = json.loads(json_content)


i = 0
user_uidList = list(user.keys())



dogbark = []


for id in user_uidList:

    if user[id]["daphnis"]["minimum"] == 0:
        user[id]["daphnis"]["minimum"] = 999


print(dogbark[:10])


with open("./src/user.json", "w") as f:
    json.dump(user, f)