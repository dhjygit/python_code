import requests
import json
import os


def search():
    os.system("clear")
    while True:
        search = input("请输入搜索关键词 (输入q;退出):\n>>>")
        os.system("clear")
        if search == "q;":
            break
        else:
            i = 0
            url = f"http://musicapi.leanapp.cn/search?keywords={search}"
            text = requests.get(url).text
            dic = json.loads(text)
            while i < len(dic["result"]["songs"]):
                result = dic["result"]["songs"][i]
                print(str(i + 1) + ". name:" + result["name"], end="   ")
                # print("id:" + str(result["id"]), end="   ")
                print("artist:" + result["artists"][0]["name"], end="   ")
                print("url:https://music.163.com/#/song?id=", end="")
                print(str(result["id"]))
                i += 1


def link():
    os.system("clear")
    while True:
        theid = input("请输入id (输入q;退出):\n>>>")
        os.system("clear")
        if theid == "q;":
            break
        else:
            print(
                f'<iframe frameborder="no" border="0" marginwidth="0" marginheight="0" width=330 height=86 src="//music.163.com/outchain/player?type=2&id={theid}&auto=1&height=66"></iframe>'
            )


while True:
    os.system("clear")
    print("==== 网易云小程序 ====")
    print("a. 搜索歌曲")
    print("b. 生成外链")
    print("q. 退出程序")
    print("==========================")
    alphabet = input("请输入对应的字母:\n>>>")
    if alphabet == "a":
        search()
    elif alphabet == "b":
        link()
    elif alphabet == "q":
        os.system("clear")
        break
    print("----------------------------------")
