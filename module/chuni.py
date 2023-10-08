import requests
import json


url = "https://www.diving-fish.com/api/chunithmprober/query/player"

music_data = requests.get("https://www.diving-fish.com/api/chunithmprober/music_data").json()



def get_chuni_b30nr10(uid):
    http_json = {"qq": str(uid)}
    r = requests.post(url, json=http_json)

    get_json = r.json()
    json_dump = json.dumps(get_json, ensure_ascii=False).encode("utf-8").decode()

    if json_dump == '{"message": "user not exists"}':
        return 404

    return_value = open("./src/temp.json", "w", encoding="utf-8").write(json_dump)
    return json.loads(json_dump)

if __name__ == "__main__":
    get_json = get_chuni_b30nr10(2154319688)
