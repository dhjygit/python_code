import requests
import json


def music():
    url = "http://web.peakchao.top:250/music/getMusicBanner"
    text = requests.get(url).text
    dic = json.loads(text)
    i = 0
    while i < len(dic["result"]):
        print("name: " + dic["result"][i]["name"], end=" - ")
        print("singer: " + dic["result"][i]["singer"])
        i += 1


music()
