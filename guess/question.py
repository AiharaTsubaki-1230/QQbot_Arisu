import random
from guess.song import song_list

def org_change(org): # 更改本家名字
    match org:
        case "arc":
            return "Arcaea"
        case "mai":
            return "maimai"
        case "chu":
            return "CHUNITHM"
        case "ongeki":
            return "オンゲキ"
        case "sdvx":
            return "SOUND VOLTEX"
        case "gc":
            return "GROOVE COASTER"
        case "iidx":
            return "beatmania IIDX"
        case "md":
            return "Muse Dash"
        case "cy":
            return "Cytus"
        case "cy2":
            return "Cytus 2"
        case "de":
            return "Deemo"
        case "la":
            return "Lanota"
        case "dy":
            return "Dynamix"
        case "voez":
            return "Voez兰空"
        case "pjsk":
            return "Project Sekai"
        case "bang":
            return "BanGDream!"
        case "taiko":
            return "太鼓の達人"
        case "ts":
            return "Tone Sphere"
        case "phi":
            return "Phigros"
    return org

def random_songs(src_list, num=10): # 随机出曲目, src是本家

    # 列表变量
    guess_song_list = [] # 猜的歌
    raw_song_list = []
    random_list = []
    org = []
    for src in src_list:
        guess_song_list.append(song_list[src])
    print(guess_song_list)
    for i in range(0, num):
        random_list.append(random.randint(0, len(src_list)-1)) # random_list = [0]
    for i in random_list:
        x = random.randint(0, len(guess_song_list[i])-1)
        while guess_song_list[i][x] in raw_song_list:
            x = random.randint(0, len(guess_song_list[i])-1)
        else:
            raw_song_list.append(guess_song_list[i][x])
            org.append(src_list[i])
    for i in range(0, len(org)):
        org[i] = org_change(org[i])
    
    hidden_song_list = []
    for i in range(0, num):
        string = ""
        for j in range(0, len(raw_song_list[i])):
            if raw_song_list[i][j] == " ":
                string = string + " "
            else:
                string = string + "-"
        hidden_song_list.append(string)
    return raw_song_list, hidden_song_list, org

def hid_songlist(raw_song_list, org):
    for i in range(0, len(org)):
        org[i] = org_change(org[i])
    hidden_song_list = []
    for i in range(0, len(raw_song_list)):
        string = ""
        for j in range(0, len(raw_song_list[i])):
            if raw_song_list[i][j] == " ":
                string = string + " "
            else:
                string = string + "-"
        hidden_song_list.append(string)
    return hidden_song_list, org