content = open("./src/bang_const.csv").readlines()

for k in range(0, len(content)):
    content[k] = content[k][:-1]

for k in range(0, len(content)):
    content[k] = content[k].split(",")
    content[k][0] = content[k][0]
    content[k][2] = float(content[k][2])

const_dict = dict()

for k in content:
    if const_dict.get(k[0]) == None:
        const_dict[k[0]] = {
            "id": k[0],
            "song_name": k[1],
            "constant": k[2]
        }
    else:
        const_dict[k[0]+"sp"] = {
            "id": k[0],
            "song_name": k[1],
            "constant": k[2]
        }

# print(content_split[1])