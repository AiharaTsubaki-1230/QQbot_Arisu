import requests
import time

token = "0c332b89f58298883d4a60d0c8704f5fa4126a0ec88c9bad76afa411eec4b8c2b9508641e9cdea73964b12bcb8b742fe46d1a72f0074354aa4708d4bcb7679c7"

import json

chuni_data = json.loads(open("./chunithm/data/data.json").read())
chuni_index = json.loads(open("./chunithm/data/data_index.json").read())

def change_diff(float_num):
    if float_num % 1 == 0.5:
        return str(int(float_num)) + "+"
    else:
        return str(int(float_num))

def csearch(search):

    url = f"https://api.chunirec.net/2.0/music/search.json?q={search}&region=jp2&token={token}"

    request = requests.get(url)

    return request.json()

def csearch_all(search):
    csearch_data = csearch(search)

    if len(csearch_data) == 1:
        id = csearch_data[0]["id"]

        url = f"https://api.chunirec.net/2.0/music/show.json?id={id}&region=jp2&token={token}"

        request = requests.get(url).json()

        msg = f"{chuni_index[request['meta']['id']]}. {request['meta']['title']}\n种类: {request['meta']['genre']}\n艺术家: {request['meta']['artist']}\nBPM: {request['meta']['bpm']}\n更新日期: {request['meta']['release']}\n"

        msg2 = "难度: "
        msg3 = "定数: "
        msg4 = "物量: "

        for diff in ["BAS", "ADV", "EXP", "MAS", "ULT"]:
            if request["data"].get(diff) == None:
                continue
            msg2 += change_diff(request["data"][diff]["level"]) + "/"
            msg3 += str(request["data"][diff]["const"]) + "/"
            msg4 += str(request["data"][diff]["maxcombo"]) + "/"
        
        msg = msg + msg2[:-1] + "\n" + msg3[:-1] + "\n" + msg4[:-1]

        return msg
    else:
        if len(csearch_data) == 0:
            return "没有搜索到符合的结果"
        else:
            msg = ""
            for data in csearch_data:
                msg += chuni_index[data["id"]] + ". " + data["title"] + "\n"
            return msg[:-1]

print(csearch_all("I'm so happy"))

def search_by_id(id):
    request = chuni_data[id]
    msg = f"{chuni_index[request['meta']['id']]}. {request['meta']['title']}\n种类: {request['meta']['genre']}\n艺术家: {request['meta']['artist']}\nBPM: {request['meta']['bpm']}\n更新日期: {request['meta']['release']}\n"

    msg2 = "难度: "
    msg3 = "定数: "
    msg4 = "物量: "

    for diff in ["BAS", "ADV", "EXP", "MAS", "ULT"]:
        if request["data"].get(diff) == None:
            continue
        msg2 += change_diff(request["data"][diff]["level"]) + "/"
        msg3 += str(request["data"][diff]["const"]) + "/"
        msg4 += str(request["data"][diff]["maxcombo"]) + "/"
    
    msg = msg + msg2[:-1] + "\n" + msg3[:-1] + "\n" + msg4[:-1]

    return msg

import re

def calc(arg1, arg2):
    regex = re.search(r"(c\d+)", arg1)
    if regex == None:
        return "格式不正确 正确格式为: /分数线 [难度][id] [目标分数]"
    id = regex.group(0)
    diff = None
    for exp in ["绿", "黄", "红", "紫", "黑"]:
        if re.search(exp, arg1) == None:
            continue
        diff = exp
    if diff == None:
        return "格式不正确 正确格式为: /分数线 [难度][id] [目标分数]"
    index = ["绿", "黄", "红", "紫", "黑"].index(diff)
    diff = ["BAS", "ADV", "EXP", "MAS", "ULT"][index]
    target = int(arg2)

    request = chuni_data[id]
    maxcombo = request["data"][diff]["maxcombo"]
    if maxcombo == 0:
        return "数据库里好像没有这张谱面的物量, 请使用/calc [物量] [目标分数]进行计算"
    
    error = 1010000 - target

    justice_deduct = 10000 // maxcombo + 1
    attack_deduct = 1010000 // (maxcombo * 2) + 1
    miss_deduct = 1010000 // maxcombo + 1

    justice_error = round(error / justice_deduct, 2)
    attack_error = round(error / attack_deduct, 2)
    miss_error = round(error / miss_deduct, 2)

    msg = f"[{diff}]{id}. {request['meta']['title']}\n目标分数:{target}\n允许最多JUSTICE数量: {justice_error}(每个-{justice_deduct})\n允许最多ATTACK数量: {attack_error}(每个-{attack_deduct})\n允许最多MISS数量: {miss_error}(每个-{miss_deduct})"
    return msg

