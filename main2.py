import json

chuni_data = json.loads(open("data.json").read())

print(chuni_data["c146"])