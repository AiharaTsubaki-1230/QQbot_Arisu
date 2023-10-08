# import requests

# request = requests.get("https://b23.tv/gOmFuUY")

# print(request.url)

# https://www.bilibili.com/video/BV1Mh4y1K7E8/?buvid=Y040DF0B1FF7C90B46EFAA3CE807F618D98A&is_story_h5=false&mid=xp0%2BVj1PNbHgvESo5bB%2B2Q%3D%3D&p=1&plat_id=116&share_from=ugc&share_medium=iphone&share_plat=ios&share_session_id=A2A2CC2E-E9C7-431A-AB43-809741909D00&sh

# import re
# import random

import time
def send_message(uid, gid, message):
    print(message)

# reg = re.search("(.+)还是(.+)", "1还是2").groups()

# flag = random.randint(0, 1)

# print("江江觉得是" + reg[flag] + "捏")

# import requests
# import time
# import random
import json

json_content = open("./src/user.json").read()
user = json.loads(json_content)
#
# uid = 114514
#
# def send_message(uid, gid, message):
#     print(uid, gid, message)
#
# init = {"today_dogbark_check": 1694908800.813613, "black_list": [624670021], "white_list": [142830249]}
#
# send_message(uid, 142830249, "chieri早")
# user_uidList = list(user.keys())
# random.shuffle(user_uidList)
# dogbark_daily = []
# for id in user_uidList:
#     dogbark_daily.append((id, user[id]["dogbark"]["today_dogbark"]))
#     dogbark_daily = sorted(dogbark_daily, key=lambda x: (x[1]), reverse=True)
#
# yesterday = time.strftime(r"%Y/%m/%d", time.localtime(time.time() - 86400))
# nickname = dogbark_daily[0][0]
# message = f"{yesterday} 的狗叫第一名是{nickname}({dogbark_daily[0][0]}), 一共狗叫了{dogbark_daily[0][1]}次"
# for group in init["white_list"]:
#     send_message(uid, group, message)

import numpy

uid = 2154319688
gid = 0

if user[str(uid)].get("daphnis") == None:
    user[str(uid)]["daphnis"] = {"length": 0, "last_time": -1, "maximum": 0, "minimum": 0, "count": 10}
if user[str(uid)]["daphnis"].get("count") == None:
    user[str(uid)]["daphnis"]["count"] = 10
print(user[str(uid)]["daphnis"]["count"])
if user[str(uid)]["daphnis"]["count"] <= 0:
    send_message(uid, gid, "今日随机次数已用完，请等待晚上12点后再来——")
if user[str(uid)]["daphnis"]["count"] == 10:
    standard_penis = round(numpy.random.normal(loc=13.12, scale=1.66), 2)
    print(user[str(uid)]["daphnis"]["count"])
    temp_penis = user[str(uid)]["daphnis"]["length"]
    user[str(uid)]["daphnis"] = {
        "length": standard_penis, "last_time": time.time(), "maximum": user[str(uid)]["daphnis"]["maximum"], "minimum": user[str(uid)]["daphnis"]["minimum"], "count": 9
    }
    standard_penis_change = round(standard_penis - temp_penis, 2)
    if standard_penis > user[str(uid)]["daphnis"]["maximum"]:
        user[str(uid)]["daphnis"]["maximum"] = standard_penis
    elif standard_penis < user[str(uid)]["daphnis"]["minimum"]:
        user[str(uid)]["daphnis"]["minimum"] = standard_penis
    message = f"你的初始几把长度为: {standard_penis}cm ({standard_penis_change})\n最长/最短: {user[str(uid)]['daphnis']['maximum']}cm/{user[str(uid)]['daphnis']['minimum']}cm\n剩余随机次数:9/10"
    send_message(uid, gid, message)
    print(user[str(uid)]["daphnis"]["count"])
elif user[str(uid)]["daphnis"]["count"] < 10:
    temp1 = user[str(uid)]["daphnis"]["count"]
    user[str(uid)]["daphnis"]["count"] = temp1 - 1

    user[str(uid)]["daphnis"]["last_time"] = time.time()
    standard_penis_change = round(numpy.random.normal(loc=0, scale=0.5), 2)
    new_penis = round(user[str(uid)]["daphnis"]["length"] + standard_penis_change, 2)
    user[str(uid)]["daphnis"]["length"] = new_penis
    if new_penis > user[str(uid)]["daphnis"]["maximum"]:
        user[str(uid)]["daphnis"]["maximum"] = new_penis
    elif new_penis < user[str(uid)]["daphnis"]["minimum"]:
        user[str(uid)]["daphnis"]["minimum"] = new_penis
    message = f"你的几把长度为: {new_penis}cm ({standard_penis_change})\n最长/最短: {user[str(uid)]['daphnis']['maximum']}cm/{user[str(uid)]['daphnis']['minimum']}cm\n剩余随机次数:{user[str(uid)]['daphnis']['count']}/10"
    send_message(uid, gid, message)

json_content_str = json.dumps(user)
open("./src/user.json", "w").write(json_content_str)