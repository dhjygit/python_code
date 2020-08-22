def exercise_one(name, lang):
    print("我是" + name + "，我爱" + lang + "")
    print("我是{}，我爱{}".format(name, lang))
    print(f"我是{name}，我爱{lang}")
    print("我是", name, "，我爱", lang, sep="")


def exercise_two():
    print(1, 2, 3, 4, 5, sep="\n")
    print("1\n2\n3\n4\n5")


def exercise_three():
    print(10, end=" ")
    print(20, end=" ")
    print(30)
