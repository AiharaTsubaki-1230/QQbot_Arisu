import requests
import module.malody as malody # ma模块
from src.get_const import const_dict # bang模块
import random
import json
import time
from guess.question import random_songs, hid_songlist, org_change
from guess.char import guess_song_char
from guess.check import check_answer, check_index
from guess.name import guess_song_name
from guess.song import song_changeLine
import module.chuni
import module.image
import chunithm.search as search
import re
import requests
from urllib.parse import quote
from html import unescape
from module.flip import img_h, img_h1, img_v, img_v1
import numpy

song_guess = dict()
flip = []
flip_arg = []

json_content = open("./src/user.json").read()
user = json.loads(json_content)

json_content_init = open("./src/init.json").read()
init = json.loads(json_content_init) 

def keyword(message, uid, gid=None, message_id=None, role=None, nickname=None):

    message = unescape(message)

    message_split = message.split(" ", 2)   

    if gid in init["black_list"]:
        return

    if gid not in init["white_list_accept"]:
        return

    # 模块1: /test
    if message == "/test" and (uid == 2676306539 or uid == 2154319688):
        send_message(uid, gid, "江江喵~")
    
    # 模块2: /江江
    if message_split[0] == "/江江":

        if user.get(str(uid)) == None:
            user[str(uid)] = {
                "gt": 0,
                "lv": 1,
                "exp": 0,
                "last_sign": 0,
                "day": 0,
                "hidden_value": 10,
                "dogbark": {
                    "dogbark_count": 0,
                    "today_dogbark": 0,
                    "last_dogbark": 0
                }
            }

        help = open("src/help.txt").read()
        response = requests.get(url=f"http://127.0.0.1:5700/get_group_member_info?user_id=3407299613&group_id={gid}").json()

        if message_split[1] == "help":
            send_message(uid, gid, help)
        
        if message_split[1] == "睡觉" and gid != None:
            if (response['data']['role'] == "admin" and role == "member") or (response['data']['role'] == "owner" and role in ["member", "admin"]):
                send_message(uid, gid, f"[CQ:reply,id={message_id}]祝你有一个充足的睡眠喵~")
                requests.get(url=f"http://127.0.0.1:5700/set_group_ban?user_id={uid}&group_id={gid}&duration=28800")
            else:
                send_message(uid, gid, f"[CQ:reply,id={message_id}]权限不足喵...")
        
        if message == "/江江 guess help":
            help = open("src/help_guess.txt").read()
            send_message(uid, gid, help)
        
        if message_split[1] == "打叠需要什么":
            send_message(uid, gid, "很多人问，打叠最需要的是什么？ 有人说是耐力，有人说是叠速。但我认为，在这两者之下更根本的，是勇气。打叠是需要勇气的，许多人看到BPM170就认为一定打不了；看到4343就认为一定拍不动，这是缺乏勇气的表现。叠力是蕴藏在身体里的抽象的能力，不去尝试，你永远不知道你有多强大的力量。BPM、密度、段位，终究只是一种量化的数字式的表现，而很多叠人却被这种数字迷惑了双眼、束缚了自我，从而缺失了面对它的勇气。不要用所谓的“我只能打BPM170以下”，“我只能打4333以下”，“我只能打delta以下”的说法禁锢自己的能力。只要有着面对的勇气，叠速、耐力、稳定，终将为你所有。用你的勇气，去领略叠键世界中的别样的风光，攀登叠键群山中的陡峭的岩壁。")

        if message_split[1] == "原神是什么":
            send_message(uid, gid, "《原神》是由米哈游自主研发的一款全新开放世界冒险游戏。游戏发生在一个被称作「提瓦特」的幻想世界，在这里，被神选中的人将被授予「神之眼」，导引元素之力‌​​​‌‌‌‌‌‌‌‌​​‌‌​‌‌‌​‌​。你将扮演一位名为「旅行者」的神秘角色，在自由的旅行中邂逅性格各异、能力独特的同伴们，和他们一起击败强敌，找回失散的亲人——同时，逐步发掘「原神」的真相。")
        
        if message_split[1] == "碧蓝档案是什么":
            send_message(uid, gid, "《碧蓝档案》是由悠星发行的一款二次元rpg游戏。游戏发生在一个被称作「基沃托斯」的幻想世界，这里的「学生」将被授予「光环」。你将扮演一位名为「老师」的神秘角色，在自由的旅行中邂逅性格各异、能力独特的同伴们，和他们一起抵抗色彩，——同时，逐步发掘「碧蓝档案」的真相。")
        
        if message_split[1] in ["签到"]:
            combo = True
            if (time.time() + 8 * 3600) // 86400 > (user[str(uid)]["last_sign"] + 8 * 3600) // 86400 + 1:
                user[str(uid)]["day"] = 0
                combo = False
            elif (time.time() + 8 * 3600) // 86400 <= (user[str(uid)]["last_sign"] + 8 * 3600) // 86400:
                send_message(uid, gid, "你已经签到过了哦~")
                return 0
            user[str(uid)]["day"] = user[str(uid)]["day"] + 1
            user[str(uid)]["last_sign"] = time.time()
            gt_add = int(user[str(uid)]["day"] * 5 + random.randint(100, 200) + user[str(uid)]["hidden_value"] * random.uniform(0.6, 0.9 + user[str(uid)]["lv"] * 0.06)) * 2
            user[str(uid)]["gt"] = user[str(uid)]["gt"] + gt_add
            exp_add = int(gt_add * random.uniform(1, 3) + user[str(uid)]["hidden_value"] * random.uniform(0.34, 0.56 + user[str(uid)]["lv"] * 0.08))
            user[str(uid)]["hidden_value"] = 0
            user[str(uid)]["exp"] = user[str(uid)]["exp"] + exp_add
            while user[str(uid)]["exp"] >= user[str(uid)]["lv"] ** 2 * 100:
                user[str(uid)]["exp"] = user[str(uid)]["exp"] - user[str(uid)]["lv"] ** 2 * 100
                user[str(uid)]["lv"] = user[str(uid)]["lv"] + 1
                user[str(uid)]["gt"] = user[str(uid)]["gt"] + user[str(uid)]["lv"] ** 2 * 8
                gt_add += user[str(uid)]["lv"] ** 2 * 8
            message = f"{nickname} Lv.{user[str(uid)]['lv']}\nEXP: {user[str(uid)]['exp']}/{user[str(uid)]['lv'] ** 2 * 100} (+{exp_add})\nGP: {user[str(uid)]['gt']}(+{gt_add})\n你已经连续签到了{user[str(uid)]['day']}天哦~"
            
            send_message(uid, gid, message)
        
        if (time.time() + 8 * 3600) // 86400 == (1693962118.432694 + 8 * 3600) // 86400 and message == "/江江 生日快乐":
            send_message(uid, gid, "谢谢捏")
            user[str(uid)]["hidden_value"] += 100
        
        if message_split[1] == "我是有栖":
            reply_list = ["我姐姐是刹那", "我是BMS精灵", "我是洛天依", "🦍🦍，我是威猛先生", "我姐姐是飞天大蟑螂", "不是，我是中二企鹅", "我是m  T: F", "我教你如何打中二节奏"]
            index = random.randint(0, len(reply_list) - 1)
            message = reply_list[index]
            send_message(uid, gid, message)
                    
        if message_split[1] == "个人信息":
            message = f"{nickname} Lv.{user[str(uid)]['lv']}\nEXP: {user[str(uid)]['exp']}/{user[str(uid)]['lv'] ** 2 * 100}\nGP: {user[str(uid)]['gt']}\n你已经连续签到了{user[str(uid)]['day']}天哦~"
            send_message(uid, gid, message)

        if message_split[1] == "头衔" and response['data']['role'] == "owner":
            requests.get(f"http://127.0.0.1:5700/set_group_special_title?group_id={gid}&user_id={uid}&special_title={message_split[2]}")

        if message_split[1] in ["狗叫", "我的狗叫", "dogbark", "db"]:
            if re.search(r"\[CQ:at,qq=(\d+)\]", message) != None:
                uid = int(re.search(r"\[CQ:at,qq=(\d+)\]", message).groups()[0])
                nickname = requests.get(f"http://127.0.0.1:5700/get_stranger_info?user_id={uid}").json()["data"]["nickname"]
            user_uidList = list(user.keys())
            random.shuffle(user_uidList)
            dogbark = []
            for id in user_uidList:
                dogbark.append((id, user[id]["dogbark"]["dogbark_count"]))
                dogbark = sorted(dogbark, key=lambda x: (x[1]), reverse=True)
            
            dogbark_data = user[str(uid)]["dogbark"]
            rank = dogbark.index((str(uid), dogbark_data["dogbark_count"])) + 1
            if rank == 1:
                previous_count = 0
            else:
                previous_count = dogbark_data["dogbark_count"] - dogbark[rank - 2][1]
                k = 0
                while previous_count == 0:
                    k += 1
                    previous_count = dogbark_data["dogbark_count"] - dogbark[rank - 2 - k][1]
            message = f'{nickname}\n狗叫排名:#{rank}/{len(user_uidList)} ({previous_count})\n总狗叫次数:{dogbark_data["dogbark_count"]}\n今日狗叫次数:{dogbark_data["today_dogbark"]}\n上次狗叫时间:{time.strftime(r"%Y/%m/%d %H:%M", time.localtime(dogbark_data["last_dogbark"]))}'
            print(message)
            send_message(uid, gid, message)
            return
        
        if message_split[1] == "我的几把":
            if re.search(r"\[CQ:at,qq=(\d+)\]", message) != None:
                uid = int(re.search(r"\[CQ:at,qq=(\d+)\]", message).groups()[0])
                nickname = requests.get(f"http://127.0.0.1:5700/get_stranger_info?user_id={uid}").json()["data"]["nickname"]
            user_uidList = list(user.keys())
            random.shuffle(user_uidList)
            dogbark = []
            for id in user_uidList:
                if user[id].get("daphnis") == None:
                    user[id]["daphnis"] = {"length": 0, "last_time": -1, "maximum": 0, "minimum": 999, "count": 0}
                if user[id]["daphnis"]["length"] == 0:
                    continue
                dogbark.append((id, user[id]["daphnis"]["length"]))
                dogbark = sorted(dogbark, key=lambda x: (x[1]), reverse=True)
            
            dogbark_data = user[str(uid)]["daphnis"]
            rank = dogbark.index((str(uid), dogbark_data["length"])) + 1
            if rank == 1:
                previous_count = 0
            else:
                previous_count = dogbark_data["length"] - dogbark[rank - 2][1]
                k = 0
                while previous_count == 0:
                    k += 1
                    previous_count = dogbark_data["length"] - dogbark[rank - 2 - k][1]
            message = f'{nickname}\n几把排名:#{rank}/{len(dogbark)} ({round(previous_count, 2)})\n你的几把长度: {dogbark_data["length"]}\n最长/最短值: {dogbark_data["maximum"]}/{dogbark_data["minimum"]}'
            print(message)
            send_message(uid, gid, message)
            return
        
        if message_split[1] == "添加关键词":
            dogbark_sentence = song_changeLine(open("./src/dogbark_temp.txt").readlines())
            dogbark_sentence.append(message_split[2])
            dogbark_string = ""
            for sent in dogbark_sentence:
                dogbark_string += sent + "\n"
            open("./src/dogbark_temp.txt", "w").write(dogbark_string[:-1])
            send_message(uid, gid, "已经添加，等待审核")
        
        if message_split[1] == "狗叫排行":
            user_uidList = list(user.keys())
            random.shuffle(user_uidList)
            dogbark = []
            message = "狗叫排行:\n"
            for id in user_uidList:
                dogbark.append((id, user[id]["dogbark"]["dogbark_count"]))
                dogbark = sorted(dogbark, key=lambda x: (x[1]), reverse=True)
            
            count = 1
            for id in dogbark[:10]:
                response = requests.get(f"http://127.0.0.1:5700/get_stranger_info?user_id={id[0]}").json()["data"]["nickname"]
                message += f"{count}. {response} - {id[1]}\n"
                count += 1
            
            message += "==========\n"

            user_dogbark = user[str(uid)]["dogbark"]["dogbark_count"]
            response = requests.get(f"http://127.0.0.1:5700/get_stranger_info?user_id={uid}").json()["data"]["nickname"]

            rank = dogbark.index((str(uid), user_dogbark)) + 1
            
            message += f"{rank}. {response} - {user_dogbark}"

            send_message(uid, gid, message)
        
        if message_split[1] == "今日狗叫排行":
            user_uidList = list(user.keys())
            random.shuffle(user_uidList)
            dogbark = []
            message = "今日狗叫排行:\n"
            for id in user_uidList:
                dogbark.append((id, user[id]["dogbark"]["today_dogbark"]))
                dogbark = sorted(dogbark, key=lambda x: (x[1]), reverse=True)
            
            count = 1
            for id in dogbark[:10]:
                response = requests.get(f"http://127.0.0.1:5700/get_stranger_info?user_id={id[0]}").json()["data"]["nickname"]
                if id[1] == 0:
                    continue
                message += f"{count}. {response} - {id[1]}\n"
                count += 1
            
            message += "==========\n"

            user_dogbark = user[str(uid)]["dogbark"]["today_dogbark"]
            response = requests.get(f"http://127.0.0.1:5700/get_stranger_info?user_id={uid}").json()["data"]["nickname"]

            rank = dogbark.index((str(uid), user_dogbark)) + 1
            
            message += f"{rank}. {response} - {user_dogbark}"

            send_message(uid, gid, message)
        
        if message_split[1] == "几把排行":
            user_uidList = list(user.keys())
            random.shuffle(user_uidList)
            dogbark = []
            message = "几把排行:\n"
            for id in user_uidList:
                if user[id].get("daphnis") == None:
                    user[id]["daphnis"] = {"length": 0, "last_time": -1, "maximum": 0, "minimum": 999, "count": 0}
                if user[id]["daphnis"]["length"] == 0 and str(uid) != id:
                    continue
                dogbark.append((id, user[id]["daphnis"]["length"]))
                dogbark = sorted(dogbark, key=lambda x: (x[1]), reverse=True)
            
            count = 1
            for id in dogbark[:10]:
                response = requests.get(f"http://127.0.0.1:5700/get_stranger_info?user_id={id[0]}").json()["data"]["nickname"]
                if id[1] == 0:
                    continue
                message += f"{count}. {response} - {id[1]}\n"
                count += 1
            
            message += "==========\n"

            user_dogbark = user[str(uid)]["daphnis"]["length"]
            response = requests.get(f"http://127.0.0.1:5700/get_stranger_info?user_id={uid}").json()["data"]["nickname"]

            rank = dogbark.index((str(uid), user_dogbark)) + 1
            
            message += f"{rank}. {response} - {user_dogbark}"

            send_message(uid, gid, message)

        if message_split[1] in ["狗叫统计", "stat"]:
            user_uidList = list(user.keys())
            total = 0
            daily = 0
            for id in user_uidList:
                total += user[id]["dogbark"]["dogbark_count"]
                daily += user[id]["dogbark"]["today_dogbark"]
            send_message(uid, gid, f"总狗叫次数:{total}\n今日总狗叫次数:{daily}")

        if re.search("(.+)还是(.+)", message_split[1]) != None:
            reg = re.search("(.+)还是(.+)", message_split[1]).groups()
            flag = int(int(time.time() * 1000) % 2)

            send_message(uid, gid, "江江觉得是" + reg[flag] + "捏")

    print(uid, gid, song_guess)

    # 模块3: /guess
    if message_split[0] == "/guess" and gid != None and re.search("-q", message) != None:
        if song_guess.get(str(gid)) == None:
            send_message(uid, gid, f"请私聊本bot并发送\n/guess question {gid} [题目的本家/出处的缩写] [你的题目] 以出题\n例如: /guess question 729529363 mai PANDORA PARADOXXX\n全部人都出完题了就输入/guess start开始吧~")
            song_guess[str(gid)] = {
                    "type": "given",
                    "raw_song": [],
                    "song_qq": [],
                    "hidden_song": [],
                    "guessed_char": "",
                    "original": [],
                    "correct": 0,
                    "input_finished": 0,
                    "answer_array": [],
                    "guess_uid": {},
                    "arg": {
                        "-u": re.search("-u", message),
                        "-v": re.search("-v", message),
                        "-lim": re.search("-lim", message),
                        "-q": None,
                        "-h": re.search("-h", message)
                    },
                    "msg_id": 0
                }
            return
        else:
            send_message(uid, gid, f"[CQ:reply,id={message_id}]这个群里已经有了猜歌题目喵~")
            return 0

        # 2: start模块 (question #2)
    if message == "/guess start" and gid != None:
        if song_guess.get(str(gid)) != None:
            if song_guess[str(gid)]["type"] == "given":
                if song_guess[str(gid)]["input_finished"] == 0:
                    song_guess[str(gid)]["input_finished"] = 1
                else:
                    return
                raw = song_guess[str(gid)]["raw_song"]
                org = song_guess[str(gid)]["original"]
                hid, org = hid_songlist(raw, org)
                song_guess[str(gid)]["hidden_song"] = hid
                song_guess[str(gid)]["original"] = org
                song_guess[str(gid)]["correct"] = len(raw)
                song_guess[str(gid)]["answer_array"] = [0 for x in range(len(raw))]
                ans_array = [0 for x in range(len(raw))]
                cor = len(raw)
                if song_guess[str(gid)]["arg"]["-lim"] == None:
                    up_lim = 10
                elif song_guess[str(gid)]["arg"]["-lim"] != None and song_guess[str(gid)]["arg"]["-u"] != None:
                    up_lim = 5
                else:
                    up_lim = 3
                if song_guess[str(gid)]["arg"]["-v"] != None:
                    guessed_char = "aeiou"
                    for char in "aeiou":
                        raw, hid, score, ans_array, cor = guess_song_char(raw, hid, char.lower(), ans_array, cor)
                        raw, hid, score, ans_array, cor = guess_song_char(raw, hid, char.upper(), ans_array, cor)
                    del score, cor
                    song_guess[str(gid)]["raw_song"] = raw
                    song_guess[str(gid)]["hidden_song"] = hid
                    song_guess[str(gid)]["guessed_char"] = guessed_char
                message = f"[Guess]\nSong guess:\nGuessed character: ({len(song_guess[str(gid)]['guessed_char'])}/{up_lim})\n"
                for i in range(0, len(hid)):
                    message += f"{i+1}. {hid[i]}\n"
                msg_id = send_message(uid, gid, message)
                song_guess[str(gid)]["msg_id"] = msg_id
                return
            else:
                send_message(uid, gid, "这个题目号码不允许自己出题哦~")
        else:
            send_message(uid, gid, "这个题目号码不存在哦") 
    
    # 3: 玩家自己输入题目的模块 (question #2)
    if message_split[0] == "/guess" and message_split[1] == "question" and gid == None:
        message_split = message.split(" ", 4)
        question_id = message_split[2]
        print(message_split)
        if song_guess.get(question_id) != None:
            if song_guess[question_id]["type"] == "given":
                if uid in song_guess[question_id]["song_qq"]:
                    send_message(uid, gid, "你已经出过题了哦~")
                    return 0
                change_line = re.search(r"\n", message)
                if change_line != None:
                    message_split[4] = message_split[4][:-1]
                raw = song_guess[question_id]["raw_song"]
                song_qq = song_guess[question_id]["song_qq"]
                org = song_guess[question_id]["original"]
                org.append(message_split[3])
                raw.append(message_split[4])
                song_qq.append(uid)
                song_guess[question_id]["raw_song"] = raw
                song_guess[question_id]["song_qq"] = song_qq
                song_guess[question_id]["original"] = org
                print(song_guess)
                send_message(uid, gid, f"出题人: {nickname}\n题目:{message_split[4]}\n本家:{org_change(message_split[3])}\n出题成功!")
                send_message(uid, int(question_id), f"题目数量+1! 现在一共有{len(raw)}个题目了喵~")
                return 
            else:
                send_message(uid, gid, "这个题目号码不允许自己出题哦~")
        else:
            send_message(uid, gid, "这个题目号码不存在哦")
    
    # 4: bot出题模块 (question) / 答题模块 + 自主出题 答题部分
    if message_split[0] == "/guess" and gid != None:
        if song_guess.get(str(gid)) == None and message_split[1] not in ["char", "name", "ans", "answer"]:
            src_list = []
            for src in ["arc", "phi", "dy", "cy2", "la", "chu", "de", "mai"]:
                if re.search(f"({src})+", message) == None:
                    continue
                src_list.append(re.search(f"({src})+", message).group(0))
            num = re.search("\d+", message)
            if num == None:
                num = 10
            else:
                num = int(num.group(0))
            if len(src_list) == 0:
                send_message(uid, gid, "你还没有输入曲库哦~")
                return 0
            print(src_list, num)
            raw, hid, org = random_songs(src_list, num)
            song_guess[str(gid)] = {
                "type": "random",
                "raw_song": raw,
                "hidden_song": hid,
                "guessed_char": "",
                "original": org,
                "correct": num,
                "guess_uid": {},
                "arg": {
                    "-u": re.search("-u", message),
                    "-v": re.search("-v", message),
                    "-lim": re.search("-lim", message),
                    "-q": None,
                    "-h": re.search("-h", message)
                },
                "msg_id": 0,
                "answer_array": [0 for x in range(num)]
            }
            print(org)
            ans_array = [0 for x in range(num)]
            cor = num
            if song_guess[str(gid)]["arg"]["-lim"] == None:
                up_lim = 10
            elif song_guess[str(gid)]["arg"]["-lim"] != None and song_guess[str(gid)]["arg"]["-u"] != None:
                up_lim = 5
            else:
                up_lim = 3
            if song_guess[str(gid)]["arg"]["-v"] != None:
                guessed_char = "aeiou"
                for char in "aeiou":
                    raw, hid, score, ans_array, cor = guess_song_char(raw, hid, char.lower(), ans_array, cor)
                    raw, hid, score, ans_array, cor = guess_song_char(raw, hid, char.upper(), ans_array, cor)
                del score, cor
                song_guess[str(gid)]["raw_song"] = raw
                song_guess[str(gid)]["hidden_song"] = hid
                song_guess[str(gid)]["guessed_char"] = guessed_char
            message = f"[Guess]\nSong guess:\nGuessed character: ({len(song_guess[str(gid)]['guessed_char'])}/{up_lim})\n"
            for i in range(0, len(hid)):
                message += f"{i+1}. {hid[i]}\n"
            message += "猜歌方式: /guess [char/name] [字母/歌名]"
            send_message(uid, gid, message)
            return
        elif song_guess.get(str(gid)) != None and  message_split[1] not in ["char", "name", "ans", "answer"]:
            send_message(uid, gid, "这个群已经有猜歌题目了哦")

        if message_split[1] in ["char"]:
            if song_guess.get(str(gid)) != None: #检测有没有群
                if song_guess[str(gid)]["arg"]["-lim"] == None:
                    up_lim = 10
                elif song_guess[str(gid)]["arg"]["-lim"] != None and song_guess[str(gid)]["arg"]["-u"] != None:
                    up_lim = 5
                else:
                    up_lim = 3
                if song_guess[str(gid)]["arg"]["-u"] != None and message_split[2] in "aeiouAEIOU":
                    send_message(uid, gid, f"[CQ:reply,id={message_id}]元音字母是不允许开的哦~")
                    return 0
                if len(song_guess[str(gid)]["guessed_char"]) >= up_lim:
                    send_message(uid, gid, f"[CQ:reply,id={message_id}]可以猜的字母数量已经到达上限了喵~")
                    return 0
                
                raw, hid, guessed_char, guess_uid = song_guess[str(gid)]["raw_song"], song_guess[str(gid)]["hidden_song"], song_guess[str(gid)]["guessed_char"], song_guess[str(gid)]["guess_uid"]
                org = song_guess[str(gid)]["original"]
                cor = song_guess[str(gid)]["correct"]
                ans_array = song_guess[str(gid)]["answer_array"]
                if message_split[2] in guessed_char:
                    send_message(uid, gid, f"[CQ:reply,id={message_id}]这个字母已经猜过了喵~")
                    return 
                guessed_char += message_split[2]
                raw, hid, score_1, ans_array, cor = guess_song_char(raw, hid, message_split[2].lower(), ans_array, cor)
                raw, hid, score_2, ans_array, cor = guess_song_char(raw, hid, message_split[2].upper(), ans_array, cor)
                message = f"[Guess]\nSong guess:({len(raw) - cor}/{len(raw)})\nGuessed char:{guessed_char}({len(guessed_char)}/{up_lim})\n"
                song_guess[str(gid)]["answer_array"] = ans_array
                for i in range(0, len(hid)):
                    if (song_guess[str(gid)]["arg"]["-h"] != None and raw[i] == hid[i]) and cor != 0:
                        continue
                    message += f"{i+1}. {hid[i]}"
                    if raw[i] == hid[i] or song_guess[str(gid)]["type"] == "given":
                        message += f" ({org[i]})"
                        if ans_array[i] != 0:
                            message += f" (#{ans_array[i]})"       
                    message += "\n"
                msg_id = send_message(uid, gid, message)
                print(msg_id)
                requests.get(f"http://127.0.0.1:5700/delete_msg?message_id={song_guess[str(gid)]['msg_id']}")
                song_guess[str(gid)]["msg_id"] = msg_id
                before_guess = song_guess[str(gid)]["guess_uid"].get(str(uid), 0)
                guess_uid[str(uid)] = before_guess + (score_1 + score_2) * 3 - 5
                song_guess[str(gid)]["raw_song"] = raw
                song_guess[str(gid)]["hidden_song"] = hid
                song_guess[str(gid)]["guessed_char"] = guessed_char
                song_guess[str(gid)]["guess_uid"] = guess_uid
            else:
                send_message(uid, gid, f"[CQ:reply,id={message_id}]这个群里还没有猜歌题目喵~")
        elif message_split[1] in ["name"]:
            if song_guess.get(str(gid)) != None:
                if song_guess[str(gid)]["type"] == "given":
                    qq_guessed = check_index(song_guess[str(gid)]["raw_song"], song_guess[str(gid)]["song_qq"], message_split[2])
                    print(qq_guessed)
                    if qq_guessed == uid:
                        return
                if song_guess[str(gid)]["arg"]["-lim"] == None:
                    up_lim = 10
                elif song_guess[str(gid)]["arg"]["-lim"] != None and song_guess[str(gid)]["arg"]["-u"] != None:
                    up_lim = 5
                else:
                    up_lim = 3
                raw, hid, guessed_char, guess_uid = song_guess[str(gid)]["raw_song"], song_guess[str(gid)]["hidden_song"], song_guess[str(gid)]["guessed_char"], song_guess[str(gid)]["guess_uid"]
                org = song_guess[str(gid)]["original"]
                cor = song_guess[str(gid)]["correct"]
                ans_array = song_guess[str(gid)]["answer_array"]
                raw, hid, flag, ans_array, cor = guess_song_name(raw, hid, message_split[2], ans_array, cor)
                message = f"[Guess]\nSong guess:({len(raw) - cor}/{len(raw)})\nGuessed char:{guessed_char}({len(guessed_char)}/{up_lim})\n"
                for i in range(0, len(hid)):
                    # 1: -h / correct
                    if (song_guess[str(gid)]["arg"]["-h"] != None and raw[i] == hid[i]) and cor != 0:
                        continue
                    message += f"{i+1}. {hid[i]}"
                    if raw[i] == hid[i] or song_guess[str(gid)]["type"] == "given":
                        message += f" ({org[i]})"
                        if ans_array[i] != 0:
                            message += f" (#{ans_array[i]})"       
                    message += "\n"
                song_guess[str(gid)]["answer_array"] = ans_array
                msg_id = send_message(uid, gid, message)
                requests.get(f"http://127.0.0.1:5700/delete_msg?message_id={song_guess[str(gid)]['msg_id']}")
                song_guess[str(gid)]["msg_id"] = msg_id
                if flag == True:
                    before_guess = song_guess[str(gid)]["guess_uid"].get(str(uid), 0)
                    guess_uid[str(uid)] = before_guess + 20
                    send_message(uid, gid, f"[CQ:reply,id={message_id}]猜对了喵~本次积分+20!")
                    if song_guess[str(gid)]["type"] == "given":
                        before_guess = song_guess[str(gid)]["guess_uid"].get(str(uid), 0)
                        correct = song_guess[str(gid)]["correct"]
                        guess_uid[str(uid)] = before_guess + 50 + correct * 3
                        before_guess = song_guess[str(gid)]["guess_uid"].get(str(qq_guessed), 0)
                        correct = song_guess[str(gid)]["correct"]
                        guess_uid[str(qq_guessed)] = before_guess - 34 - correct * 2
                        send_message(uid, gid, f"自主出题额外加减分:\n[CQ:at,qq={uid}] +{50+correct*3}\n[CQ:at,qq={qq_guessed}] {-34-correct*2}")

                else:
                    send_message(uid, gid, f"[CQ:reply,id={message_id}]你猜的答案并不正确喵，请再想想喵~")
                    before_guess = song_guess[str(gid)]["guess_uid"].get(str(uid), 0)
                    guess_uid[str(uid)] = before_guess - 10
                
                song_guess[str(gid)]["raw_song"] = raw
                song_guess[str(gid)]["hidden_song"] = hid
                song_guess[str(gid)]["guessed_char"] = guessed_char
                song_guess[str(gid)]["guess_uid"] = guess_uid
            else:
                send_message(uid, gid, f"[CQ:reply,id={message_id}]这个群里还没有猜歌题目喵~")
        elif message_split[1] in ["answer", "ans"]:
            if song_guess.get(str(gid)) != None:
                if song_guess[str(gid)]["arg"]["-lim"] == None:
                    up_lim = 10
                elif song_guess[str(gid)]["arg"]["-lim"] != None and song_guess[str(gid)]["arg"]["-u"] != None:
                    up_lim = 5
                else:
                    up_lim = 3
                raw, hid, guessed_char, guess_uid = song_guess[str(gid)]["raw_song"], song_guess[str(gid)]["hidden_song"], song_guess[str(gid)]["guessed_char"], song_guess[str(gid)]["guess_uid"]
                org = song_guess[str(gid)]["original"]
                ans_array = song_guess[str(gid)]["answer_array"]
                message = f"[Guess]\nAnswer:\nGuessed char:{guessed_char}({len(guessed_char)}/{up_lim})\n"
                for i in range(0, len(hid)):
                    message += f"{i+1}. {raw[i]} ({org[i]})"
                    if ans_array[i] != 0:
                        message += f" (#{ans_array[i]})"
                    message += "\n"
                requests.get(f"http://127.0.0.1:5700/delete_msg?message_id={song_guess[str(gid)]['msg_id']}")
                msg_id = send_message(uid, gid, message)
                song_guess[str(gid)]["raw_song"] = raw
                song_guess[str(gid)]["hidden_song"] = hid
                song_guess[str(gid)]["guessed_char"] = guessed_char
                song_guess[str(gid)]["guess_uid"] = guess_uid
                song_guess[str(gid)]["correct"] = 0
                song_guess[str(gid)]["msg_id"] = msg_id
            else:
                send_message(uid, gid, f"[CQ:reply,id={message_id}]这个群里还没有猜歌题目喵~")
        if song_guess.get(str(gid)) != None:
            if song_guess[str(gid)]["correct"] != 0:
                flag, num_of_correct = check_answer(song_guess[str(gid)]["raw_song"], song_guess[str(gid)]["hidden_song"])
                print(num_of_correct)
                song_guess[str(gid)]["correct"] = num_of_correct
            else:
                flag = False
        else:
            flag = False
            return
        if flag:
            send_message(uid, gid, "全部题目都已经被猜出来了喵")
        if song_guess[str(gid)]["correct"] == 0 or flag:
            song_guess.pop(str(gid))
            message = "[Guess]\n本次猜歌总分:\n"
            guess_uid_list = list(guess_uid.keys())
            for i in guess_uid_list:
                if user.get(i) == None:
                    user[i] = {
                        "gt": 0,
                        "lv": 1,
                        "exp": 0,
                        "last_sign": 0,
                        "day": 0,
                        "hidden_value": 10,
                        "dogbark": {
                            "dogbark_count": 0,
                            "today_dogbark": 0,
                            "last_dogbark": 0
                        }
                    }
                message += f"[CQ:at,qq={int(i)}]: {guess_uid[i]}\n"
                user[i]["gt"] = round(user[i]["gt"] + (guess_uid[i]) * round(random.uniform(1, 4), 1), 1)
                user[i]["hidden_value"] = round(user[i]["hidden_value"] + (guess_uid[i]) * random.uniform(0.3, user[i]["lv"] * 0.05 + 0.4), 1)
            print(message)
            send_message(uid, gid, message)

    # 模块4: ma 查分
    if message_split[0] == "/ma":
        message_split[2] = message_split[2].split("-", 1)
        if message_split[2][0] == "reg":
            dan = int(message_split[2][1])
        acc, final_acc = malody.get_acc(message_split[1], dan)
        message = f"[CQ:reply,id={message_id}]Malody单曲acc查询:\n段位:{message_split[2][0]}-{message_split[2][1]}\n你的第一首acc是:{acc[0]}%\n你的第二首acc是:{acc[1]}%\n你的第三首acc是:{acc[2]}%\n你的第四首acc是:{acc[3]}%"
        if message_split[2][0] == "reg" and final_acc >= 95.00:
            message += "\n恭喜过段喵~"
        elif message_split[2][1] == "ex" and final_acc >= 96.00:
            message += "\n恭喜过段喵~"
        send_message(uid, gid, message)
    
    # 模块5: 查询邦定数
    if message_split[0] == "/bang":
        message_split = message.split(" ", 4)
        if message_split[1] == "const":
            const = const_dict[message_split[2]]
            print(const, message_split[2])
            send_message(uid, gid, f"{message_split[2]}. {const['song_name']}\n定数:{const['constant']}")
        if message_split[1] == "random":
            if len(message_split) != 5:
                send_message(uid, gid, "输入的参数不足哦~\n格式是/bang random [最小定数] [最大定数] [随机的数量]")
            else:
                max_const = float(message_split[3])
                min_const = float(message_split[2])

                random_song = []
                const_sum = 0
                print(min_const, max_const)
                while len(random_song) < int(message_split[4]):
                    index = random.randint(1, 457)
                    sp = random.randint(0, 3)
                    if index and index not in [6, 23, 38, 39, 98, 99, 102, 103, 114, 196, 216, 273, 367, 368, 369, 377, 385, 454]:
                        test_sp = const_dict.get(str(index)+"sp")
                        if test_sp != None and sp == 3:
                            index = str(index) + "sp"
                        if min_const <= const_dict[str(index)]["constant"] and const_dict[str(index)]["constant"] <= max_const:
                            random_song.append(const_dict[str(index)])
                            const_sum += const_dict[str(index)]["constant"]
                            print(const_dict[str(index)])
                            if len(random_song) == int(message_split[4]):
                                print(const_sum / int(message_split[4]))
                                if const_sum / int(message_split[4]) <= ((max_const + min_const) / 2 - 0.05):
                                    random_song = []
                                    const_sum = 0
                message = ""
                for song in random_song:
                    message += f"{song['id']}. {song['song_name']}\n定数: {song['constant']}\n"
                send_message(uid, gid, message)
    
    if message == "/b30":
        send_message(uid, gid, "查你妈b30😠, 不如/chu b30")
        # req = module.chuni.get_chuni_b30nr10(uid)
        # if req == 404:
        #     send_message(uid, gid, "你还未绑定哦~")
        # else:
        #     img = module.image.draw_b30_img(req)
        #     img.save("/Users/a1231/data/images/temp_b30.png")
        #     send_message(uid, gid, f"[CQ:image,file=temp_b30.png]")
    
    if message in ["/今日运势", "/jrys"]:
        jrys_list = ['拼机', '推分', '越级', '下埋', '夜勤', '练底力', '练手法', '干饭', '收歌', '炫DQ', '开键盘歌', '开猩猩歌', '开特大']
        if user.get(str(uid)) == None:
            user[str(uid)] = {
                "gt": 0,
                "lv": 1,
                "exp": 0,
                "last_sign": 0,
                "day": 0,
                "hidden_value": 10,
                "jrys": {
                    "宜": [],
                    "不宜": [],
                    "last_jrys": 0
                },
                "dogbark": {
                    "dogbark_count": 0,
                    "today_dogbark": 0,
                    "last_dogbark": 0
                }
            }
        if user[str(uid)].get("jrys") == None:
            user[str(uid)]["jrys"] = {
                "宜": [],
                "不宜": [],
                "last_jrys": 0
            }
        last_jyrs = user[str(uid)]["jrys"]["last_jrys"]

        if (time.time() + 8 * 3600) // 3600 <= (last_jyrs + 8 * 3600) // 3600:
            send_message(uid, gid, "你已经抽取过了哦，请过一会再来吧~")
            return
        else:
            jrys = []
            flag = False
            for i in range(4):
                jrys_seed = random.randint(0, len(jrys_list) - 1)
                while jrys_list[jrys_seed] in jrys:
                    jrys_seed = random.randint(0, len(jrys_list) - 1)
                jrys.append(jrys_list[jrys_seed])
            user[str(uid)]["jrys"] = {
                "宜": jrys[0:1],
                "不宜": jrys[2:3],
                "lucky_number": random.randint(1, 100),
                "last_jrys": time.time()
            }
            message = f"您的今日运势如下:\n宜:{jrys[0]},{jrys[1]}\n不宜:{jrys[2]},{jrys[3]}\n幸运数字为:{user[str(uid)]['jrys']['lucky_number']}"
            user[str(uid)]["hidden_value"] = round(user[str(uid)]["hidden_value"] + user[str(uid)]['jrys']['lucky_number'] * random.uniform(1, 3), 1)
            send_message(uid, gid, message)

    if re.search("/抢夺", message) != None:
        get_qq = int(re.search(r"\[CQ:at,qq=(\d+)\]", message).groups()[0])
        seed = random.randint(0, 100)
        if user.get(str(uid)) == None:
            user[str(uid)] = {
                "gt": 0,
                "lv": 1,
                "exp": 0,
                "last_sign": 0,
                "day": 0,
                "hidden_value": 10,
                "jrys": {
                    "宜": [],
                    "不宜": [],
                    "last_jrys": 0
                },
                "dogbark": {
                    "dogbark_count": 0,
                    "today_dogbark": 0,
                    "last_dogbark": 0
                }
            }
        if user.get(str(get_qq)) == None:
            user[str(get_qq)] = {
                "gt": 0,
                "lv": 1,
                "exp": 0,
                "last_sign": 0,
                "day": 0,
                "hidden_value": 10,
                "jrys": {
                    "宜": [],
                    "不宜": [],
                    "last_jrys": 0
                },
                "dogbark": {
                    "dogbark_count": 0,
                    "today_dogbark": 0,
                    "last_dogbark": 0
                }
            }
        seed_qq1 = random.uniform(0.5, 3)
        if user[str(uid)]["gt"] <= 0:
            hidden = random.randint(5, 20)
        else:
            hidden = 0
        if seed >= 50:
            seed_1 = ( (seed - 50) / 3 ) ** 2
            get_qq_gt = abs(user[str(uid)]["gt"])
            get_gt = int(get_qq_gt // 10 * ( seed_1 / 1250 ) * 5)
            response = requests.get(f"http://127.0.0.1:5700/get_stranger_info?user_id={get_qq}").json()["data"]["nickname"]
            print(response)
            message = f"{seed} >= 50, 抢夺成功\n{response} -{int(get_gt * seed_qq1)}GP\n{nickname} +{int(get_gt * seed_qq1)}GP"
            user[str(uid)]["gt"] = int(user[str(uid)]["gt"] + get_gt * seed_qq1 + hidden)
            user[str(uid)]["hidden_value"] = int(user[str(uid)]["hidden_value"] + get_gt * 1.2 // 50 + 1)
            user[str(get_qq)]["gt"] = int(user[str(get_qq)]["gt"] - get_gt * seed_qq1)
        else:
            seed_1 = ( (50 - seed) // 3 ) ** 2
            get_qq_gt = abs(user[str(uid)]["gt"])
            get_gt = int(get_qq_gt // 10 * ( seed_1 / 1250 ) * 5)
            response = requests.get(f"http://127.0.0.1:5700/get_stranger_info?user_id={get_qq}").json()["data"]["nickname"]
            print(response)
            message = f"{seed} < 50, 抢夺失败\n{response} +{int(get_gt * seed_qq1)}GP\n{nickname} -{int(get_gt * seed_qq1)}GP"
            user[str(uid)]["gt"] = int(user[str(uid)]["gt"] - get_gt * seed_qq1 + hidden)
            user[str(get_qq)]["hidden_value"] = int(user[str(get_qq)]["hidden_value"] + get_gt * 1.2 // 50 + 1)
            user[str(get_qq)]["gt"] = int(user[str(get_qq)]["gt"] + get_gt * seed_qq1)
        send_message(uid, gid, message)

    if message_split[0] == "/flip" and uid not in flip:
        if len(message_split) != 3:
            message_split = ["/flip", "h", "0"]

        flip.append(uid)
        flip_arg.append((message_split[1], message_split[2]))
        send_message(uid, gid, "请发送图片")

    if uid in flip and re.search("CQ:image", message) != None:
        reg = re.search("url=(.+)]", message)
        url = reg.groups()[0]

        print(url)

        index = flip.index(uid)
        arg = flip_arg[index]
        flip.pop(index)
        flip_arg.pop(index)
    
        request = requests.get(url)


        open('./src/temp1.png', 'wb').write(request.content)

        img_url = "./src/temp1.png"


        print(img_url)

        match arg:
            case ("h", "0"):
                img_h(img_url)
            case ("v", "0"):
                img_v(img_url)
            case ("h", "1"):
                img_h1(img_url)
            case ("v", "1"):
                img_v1(img_url)
        
        send_message(uid, gid, "[CQ:image,file=temp.png]")
    
    # if message == "/随机几把":
    #     if user[str(uid)].get("daphnis") == None:
    #         user[str(uid)]["daphnis"] = {"length": 0, "last_time": -1, "maximum": 0, "minimum": 999, "count": 10}
    #     if user[str(uid)]["daphnis"]["count"] <= 0:
    #         send_message(uid, gid, "今日随机次数已用完，请等待晚上12点后再来——")
    #         return
    #     if user[str(uid)]["daphnis"]["count"] == 10:
    #         standard_penis = round(numpy.random.normal(loc=13.12, scale=1.66), 2)
    #         user[str(uid)]["daphnis"]["count"] = 9
    #         temp_penis = user[str(uid)]["daphnis"]["length"]
    #         user[str(uid)]["daphnis"]["length"] = standard_penis
    #         user[str(uid)]["daphnis"]["last_time"] = time.time()
    #         standard_penis_change = round(standard_penis - temp_penis, 2)
    #         if standard_penis > user[str(uid)]["daphnis"]["maximum"]:
    #             user[str(uid)]["daphnis"]["maximum"] = standard_penis
    #         if standard_penis < user[str(uid)]["daphnis"]["minimum"]:
    #             user[str(uid)]["daphnis"]["minimum"] = standard_penis
    #         message = f"你的初始几把长度为: {standard_penis}cm ({standard_penis_change})\n最长/最短: {user[str(uid)]['daphnis']['maximum']}cm/{user[str(uid)]['daphnis']['minimum']}cm\n剩余随机次数:9/10"
    #         send_message(uid, gid, message)
    #     elif user[str(uid)]["daphnis"]["count"] < 10:
    #         temp1 = user[str(uid)]["daphnis"]["count"]
    #         user[str(uid)]["daphnis"]["count"] = temp1 - 1

    #         user[str(uid)]["daphnis"]["last_time"] = time.time()
    #         standard_penis_change = round(numpy.random.normal(loc=0, scale=0.5), 2)
    #         new_penis = round(user[str(uid)]["daphnis"]["length"] + standard_penis_change, 2)
    #         user[str(uid)]["daphnis"]["length"] = new_penis
    #         if new_penis > user[str(uid)]["daphnis"]["maximum"]:
    #             user[str(uid)]["daphnis"]["maximum"] = new_penis
    #         if new_penis < user[str(uid)]["daphnis"]["minimum"]:
    #             user[str(uid)]["daphnis"]["minimum"] = new_penis
    #         message = f"你的几把长度为: {new_penis}cm ({standard_penis_change})\n最长/最短: {user[str(uid)]['daphnis']['maximum']}cm/{user[str(uid)]['daphnis']['minimum']}cm\n剩余随机次数:{user[str(uid)]['daphnis']['count']}/10"
    #         send_message(uid, gid, message)

    # chunithm

    if message_split[0] == "/search":
        message = search.csearch_all(message_split[1])
        send_message(uid, gid, message)

    if message_split[0] == "/id":
        message = search.search_by_id(message_split[1])
        send_message(uid, gid, message)

    if message_split[0] == "/分数线":
        message = search.calc(message_split[1], message_split[2])
        send_message(uid, gid, message)

    # 狗叫
    dogbark_sentence = song_changeLine(open("./src/dogbark.txt").readlines())


    dogbark_flag = False

    if uid in init["dogbark_permit"]:
        dogbark_flag = True

    print(dogbark_sentence)

    for dogbark in dogbark_sentence:
        if re.search(dogbark, message) != None or (re.search(dogbark, nickname) != None and init["nickname"]):
            dogbark_flag = True
            print(dogbark)
            break
    
    today_dogbark_check = init["today_dogbark_check"]

    if (time.time() + 8 * 3600) // 86400 != today_dogbark_check // 86400:
        today_dogbark_check = time.time() + 8 * 3600
        init["today_dogbark_check"] = today_dogbark_check
        send_message(uid, 142830249, "chieri早")
        with open("./src/init.json", "w") as f:
            json.dump(init, f)
        user_uidList = list(user.keys())
        random.shuffle(user_uidList)
        dogbark_daily = []

        for id in user_uidList:
            dogbark_daily.append((id, user[id]["dogbark"]["today_dogbark"]))
            dogbark_daily = sorted(dogbark_daily, key=lambda x: (x[1]), reverse=True)
            if user[id].get("daphnis") == None:
                user[id]["daphnis"] = {"length": 0, "last_time": -1, "maximum": 0, "minimum": 999, "count": 10}
            user[id]["daphnis"]["length"] = 0
            user[id]["daphnis"]["count"] = 10


        yesterday = time.strftime(r"%Y/%m/%d", time.localtime(time.time() - 86400))
        nickname = requests.get(f"http://127.0.0.1:5700/get_stranger_info?user_id={dogbark_daily[0][0]}").json()["data"]["nickname"]
        message = f"{nickname}({dogbark_daily[0][0]})是昨天({yesterday})的狗叫王, 一共狗叫了{dogbark_daily[0][1]}次, 恭喜捏"
        

        if dogbark_daily[0][0] == init["dogbark_daily"]["uid"]:
            days = init["dogbark_daily"]["days"] + 1
        else:
            days = 1

        init["dogbark_daily"] = {"uid": dogbark_daily[0][0], "days": days}
        for group in init["white_list"]:
            # send_message(uid, group, message)
            send_message(uid, group, message)
            print(111)
        for id in user_uidList:
            user[id]["hidden_value"] = user[id]["hidden_value"] + int(user[id]["dogbark"]["today_dogbark"] * (user[id]["lv"] ** 2) // 10)
            user[id]["dogbark"]["today_dogbark"] = 0

    if dogbark_flag:
        if user.get(str(uid)) == None:
            user[str(uid)] = {
                "gt": 0,
                "lv": 1,
                "exp": 0,
                "last_sign": 0,
                "day": 0,
                "hidden_value": 10,
                "jrys": {
                    "宜": [],
                    "不宜": [],
                    "last_jrys": 0
                },
                "dogbark": {
                    "dogbark_count": 0,
                    "today_dogbark": 0,
                    "last_dogbark": 0
                }
            }
        user[str(uid)]["dogbark"]["dogbark_count"] += 1
        user[str(uid)]["dogbark"]["today_dogbark"] += 1
        user[str(uid)]["dogbark"]["last_dogbark"] = time.time()
        print("狗叫")
        
    init["today_dogbark_check"] = today_dogbark_check

    if int(time.time()) % 15 <= 3:
        json_content_str = json.dumps(user)
        open("./src/user.json", "w").write(json_content_str)
        
        with open("./src/init.json", "w") as f:
            json.dump(init, f)

# send_message
def send_message(uid, gid, message):
    message = quote(message)
    if gid == None:
        msg_id = requests.get(url="http://127.0.0.1:5700/send_private_msg?user_id={0}&message={1}".format(uid, message))
    else:
        msg_id = requests.get(url="http://127.0.0.1:5700/send_group_msg?group_id={0}&message={1}".format(gid, message))
    msg_json = msg_id.json()
    return msg_json["data"]["message_id"]