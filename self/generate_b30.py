content = open("./src/kurokob30.csv", "r", encoding="utf-8").readlines()

b30 = {}

import json

def calc_b30(c, s):
    if s >= 9800000:
        s -= 9800000
        return c + 1 + s / 200000
    else:
        s -= 9500000
        return c + s / 300000

for i in content:
    i = i[:-1].split(",")
    b30[i[0]] = {
        "song": i[0],
        "const": float(i[1]),
        "score": int(i[2]),
        "ptt": round(calc_b30(float(i[1]), int(i[2])), 4)
    }

open("./src/b30_2154319688.json", "w").write(json.dumps(b30))
