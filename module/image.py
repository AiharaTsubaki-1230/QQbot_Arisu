from PIL import Image, ImageDraw, ImageFont
import json
import re
import requests

font = ImageFont.truetype("./../src/yezigongchangquqiti.ttf", 65)
font_2 = ImageFont.truetype("./../src/yezigongchangquqiti.ttf", 55)
font_3 = ImageFont.truetype("./../src/KaiseiOpti-Regular.ttf", 35)

chuni_music = json.loads(open("./src/chuni_music.json").read())

def get_bg(title):
    for music in chuni_music:
        if title == music["title"]:
            return music["image"]

def draw_b30_img(b30):
    # 图片
    username = b30["nickname"]
    rating = round(b30["rating"], 2)

    b30_avg = 0
    for b30_data in b30["records"]["b30"]:
        b30_avg += b30_data["ra"]
    
    b30_avg = round(b30_avg / 30, 4)

    r10_avg = 0
    for r10_data in b30["records"]["r10"]:
        r10_avg += r10_data["ra"]
    
    r10_avg = round(r10_avg / 10, 4)

    img = Image.new("RGB", (2640, 2050), (30, 30, 30))

    draw = ImageDraw.Draw(img)
    draw_transp = ImageDraw.Draw(img, "RGBA")

    draw.text((50, 50), f"{username} / Rating: {rating} \nB30: {b30_avg} / R10: {r10_avg}", "white", font=font)

    draw.line([(50, 190), (2590, 190)], fill="white", width = 10)

    for i in range(30):

        b30_song_data = b30["records"]["b30"][i]

        height_1 = 200 + (i // 5) * 220
        height_2 = height_1 + 210
        width_1 = 50 + (i % 5) * 510
        width_2 = width_1 + 500
        print([(width_1, height_1), (width_2, height_2)])

        bg_url = "https://new.chunithm-net.com/chuni-mobile/html/mobile/img/" + get_bg(b30_song_data["title"])
        request = requests.get(bg_url)
        open('./src/temp.png', 'wb').write(request.content)
        bg = Image.open("./src/temp.png")

        bg = bg.resize((500, 500))
        bg = bg.crop((0, 50, 500, 260))
        img.paste(bg, (width_1, height_1))

        draw_transp.rectangle([(width_1, height_1), (width_2, height_2)], fill=(0, 0, 0, 150))
        
        reg = re.compile("([a-zA-Z0-9 ])")
        reg = len(reg.findall(b30_song_data["title"]))
        total_length = len(b30_song_data["title"]) * 2 - reg * 1.2

        if total_length >= 16:
            title = b30_song_data["title"][:13] + ".."
        else:
            title = b30_song_data["title"]
        draw.text((width_1 + 5, height_1 + 5), title, "white", font=font_3)

        if b30_song_data["level_label"] == "Master":
            color = "#8866ff"
        elif b30_song_data["level_label"] == "Expert":
            color = "#ff2200"


        draw.rectangle([(width_2 - 170, height_1 + 5), (width_2 - 5, height_1 + 70)], fill=color)

        draw.text((width_2 - 165, height_1 + 10), b30_song_data["level_label"][:3] + b30_song_data["level"], "white", font=font_2)
        draw.text((width_1 + 5, height_1 + 75), str(b30_song_data["score"]), "white", font=font_2)
        draw.text((width_1 + 5, height_1 + 140), f"Rating: {b30_song_data['ds']} -> {b30_song_data['ra']}", "white", font=font_2)

    draw.line([(50, 1520), (2590, 1520)], fill="white", width = 10)

    for i in range(10):
        b30_song_data = b30["records"]["r10"][i]
        height_1 = 1530 + (i // 5) * 220
        height_2 = height_1 + 210
        width_1 = 50 + (i % 5) * 510
        width_2 = width_1 + 500
        print([(width_1, height_1), (width_2, height_2)])

        bg_url = "https://new.chunithm-net.com/chuni-mobile/html/mobile/img/" + get_bg(b30_song_data["title"])
        request = requests.get(bg_url)
        open('./src/temp.png', 'wb').write(request.content)
        bg = Image.open("./src/temp.png")

        bg = bg.resize((500, 500))
        bg = bg.crop((0, 50, 500, 260))
        img.paste(bg, (width_1, height_1))

        reg = re.compile("([a-zA-Z0-9 ])")
        reg = len(reg.findall(b30_song_data["title"]))
        total_length = len(b30_song_data["title"]) * 2 - reg * 1.2
        if total_length >= 16:
            title = b30_song_data["title"][:13] + ".."
        else:
            title = b30_song_data["title"]

        draw_transp.rectangle([(width_1, height_1), (width_2, height_2)], fill=(0, 0, 0, 150))

        draw.text((width_1 + 5, height_1 + 5), title, "white", font=font_3)

        if b30_song_data["level_label"] == "Master":
            color = "#8866ff"
        elif b30_song_data["level_label"] == "Expert":
            color = "#ff2200"

        draw.rectangle([(width_2 - 170, height_1 + 5), (width_2 - 5, height_1 + 70)], fill=color)

        draw.text((width_2 - 165, height_1 + 10), b30_song_data["level_label"][:3] + b30_song_data["level"], "white", font=font_2)
        draw.text((width_1 + 5, height_1 + 75), str(b30_song_data["score"]), "white", font=font_2)
        draw.text((width_1 + 5, height_1 + 140), f"Rating: {b30_song_data['ds']} -> {b30_song_data['ra']}", "white", font=font_2)
    return img

if __name__ == "__main__":
    b30 = json.loads(open("src/temp.json").read())
    return_b30_img = draw_b30_img(b30)
    return_b30_img.show()