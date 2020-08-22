import os
import time
import random
import function

os.system("clear")
print("===== guess number =====")
print("*1.开始游戏  *2.游戏规则")
print("*3.退出游戏")
print("========================")
_input = input("请输入数字选择菜单:\n>>>")
while True:
    os.system("clear")
    print("===== guess number =====")
    print("*1.开始游戏  *2.游戏规则")
    print("*3.退出游戏")
    print("========================")
    if _input == "1":
        function.games()
        _input = input("请输入数字选择菜单:\n>>>")
    elif _input == "2":
        function.regular()
        _input = input("请输入数字选择菜单:\n>>>")
    elif _input == "3":
        break
    else:
        _input = input("输入格式错误，请重新输入数字选择菜单:\n>>>")
os.system("clear")
