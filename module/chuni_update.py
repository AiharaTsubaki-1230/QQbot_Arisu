import requests

token = "0c332b89f58298883d4a60d0c8704f5fa4126a0ec88c9bad76afa411eec4b8c2b9508641e9cdea73964b12bcb8b742fe46d1a72f0074354aa4708d4bcb7679c7"

def data_showall():

    url = f"https://api.chunirec.net/2.0/music/showall.json?region=jp2&token={token}"

    request = requests.get(url)

    return request.json()

code = 1
code_we = 10001

import json

chuni = {}
chuni_code = {}

for chuni_data in data_showall():

    if chuni_data["meta"]["genre"] == "WORLD'S END":
        num = code_we
        code_we += 1
    else:
        num = code
        code += 1
    chuni["c" + str(num)] = chuni_data

code = 1
code_we = 10001


for chuni_data in data_showall():
    if chuni_data["meta"]["genre"] == "WORLD'S END":
        num = code_we
        code_we += 1
    else:
        num = code
        code += 1
    chuni_code[chuni_data["meta"]["id"]] = "c" + str(num)
    
string = json.dumps(chuni)

open("data.json", "w").write(string)
open("data_index.json", "w").write(json.dumps(chuni_code))