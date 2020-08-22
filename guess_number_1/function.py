import os
import time
import random


def games():
    os.system("clear")
    true_false = True
    score = []
    cycle = 0
    while true_false:
        os.system("clear")
        guess_number = random.randint(0, 0)
        begin_time = time.time()
        input_number = input("请输入您猜测的数字(返回菜单请按q):\n>>>")
        count = 1
        origin_count = 3
        while count < origin_count:
            if input_number == "q":
                true_false = False
                break
            elif input_number.isdigit() and int(input_number) == guess_number:
                print("猜测正确")
                break
            elif input_number.isdigit(
            ) and int(input_number) > guess_number and int(input_number) < 10:
                input_number = input("数字太大, 请重新输入(返回菜单请按q):\n>>>")
            elif input_number.isdigit(
            ) and int(input_number) < guess_number and int(input_number) < 10:
                input_number = input("数字太小, 请重新输入(返回菜单请按q):\n>>>")
            else:
                input_number = input("输入格式错误，请重新输入数字(返回菜单请按q):\n>>>")
                origin_count += 1
            count += 1
        cycle += 1
        end_time = time.time()
        used_time = round(end_time - begin_time, 2)
        result = True if input_number == str(guess_number) else False
        score.append((cycle, result, used_time))
        print("========= score ==========")
        best_score = min(score, key=lambda x: x[2])
        worst_score = max(score, key=lambda x: x[2])
        for _cycle, _result, _used_time in score:
            best_label = "best" if _used_time == best_score[
                2] and cycle != 1 else ""
            worst_label = "worst" if _used_time == worst_score[
                2] and cycle != 1 else ""
            print(
                f"第{_cycle}轮  {_result}  {_used_time}秒 {best_label}{worst_label}"
            )
        print("==========================")
        if true_false:
            game_over = input(f"第{cycle}轮游戏结束(按y开始下一轮游戏，按n或q退出游戏):")
            while True:
                if game_over == "n" or game_over == "q":
                    true_false = False
                    break
                elif game_over == "y":
                    break
                else:
                    game_over = input("输入格式错误，请重新输入(按y开始下一轮游戏，按n或q退出游戏):")
        else:
            break
    os.system("clear")
    print("===== guess number =====")
    print("*1.开始游戏  *2.游戏规则")
    print("*3.退出游戏")
    print("========================")


def regular():
    os.system("clear")
    print("游戏规则：")
    print("    系统随机生成0到9中")
    print("的任意一个数字，并将由")
    print("玩家输入猜测的数字，如")
    print("果玩家输入的数字与系统")
    print("随机生成的数字相同，则")
    print("该轮游戏胜利，每轮有3")
    print("次机会。")
    input("---按任意键返回菜单---")
    os.system("clear")
    print("===== guess number =====")
    print("*1.开始游戏  *2.游戏规则")
    print("*3.退出游戏")
    print("========================")
