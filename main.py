import requests

token = "0c332b89f58298883d4a60d0c8704f5fa4126a0ec88c9bad76afa411eec4b8c2b9508641e9cdea73964b12bcb8b742fe46d1a72f0074354aa4708d4bcb7679c7"

# search


def csearch(search):

    url = f"https://api.chunirec.net/2.0/music/search.json?q={search}&region=jp2&token={token}"

    request = requests.get(url)

    return request.json()


'''
[
{
    "title": "The wheel to the right",
    "genre": "ORIGINAL",
    "artist": "Sampling Masters MEGA",
    "release": "2015-07-17",
    "id": "e5569e1702c8020e"
},
{
    "title": "Yet Another ”drizzly rain”",
    "genre": "東方Project",
    "artist": "myu314 feat.あまね（COOL&CREATE）",
    "release": "2015-11-12",
    "id": "2ca61b1981ba9c2f"
},
{
    "title": "The Other Side of the Wall",
    "genre": "POPS&ANIME",
    "artist": "Void_Chords feat.MARU",
    "release": "2019-08-22",
    "id": "82a0ed789bf9789a"
}
]
'''


def csearch_all(search):
    csearch_data = csearch(search)

    if len(csearch_data) == 1:
        id = csearch_data[0]["id"]

        url = f"https://api.chunirec.net/2.0/music/show.json?id={id}&region=jp2&token={token}"

        request = requests.get(url)

        return request.json()
    else:
        if len(csearch_data) == 0:
            return "没有搜索到符合的结果"
        else:
            return csearch_data


print(csearch_all("the"))
