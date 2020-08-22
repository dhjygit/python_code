# id()
# 地址

print("python", "python", sep=" ", end="\n")

round(3.1415926, 2)
print("python".ljust(10, "|"))

"the python".upper()
"the python".lower()
"the python".title()
"the python".capitalize()  # "The python"
"THE python".swapcase()  # "the PYTHON"

"THE PYTHON".isupper()
"the python".islower()
"The Python".istitle()

"".isalpha()
"".isdigit()
"".isalnum()
"".isascii()
"".isspace()
# isalpha,isalnum包括中文

int("1")
str(1)

max([1, 4], [4, 1], key=lambda x: x[0] if True else x[1])
min([1, 4], [4, 1], key=lambda x: x[0] if True else x[1])

map_tuple = map(lambda x, y: x + y, (1, 2, 3, 4, 5), (1, 2, 3, 4, 5))
map_list = map(lambda x, y: x + y, [1, 2, 3, 4, 5], [1, 2, 3, 4, 5])
tuple(map_tuple)
list(map_list)

"python".find("n", 0, 6)
"python".index("n", 0, 6)
range(1, 4).index(3)
(1, 2, 3, 4).index(4)
[1, 2, 3, 4].index(4)
# .find()  只能搜索str: 且搜索不到结果将返回-1
# .index()  能搜索str,range(),(),[]: 且搜索不到结果将发生错误
# 括号搜索内容的后面两个参数，第一个起始位置，第二次终止位置，前闭后开

for index, char in enumerate("python", 0):
    pass
for index, number in enumerate(range(1, 4), 0):
    pass
for index, number in enumerate((1, 2, 3), 0):
    pass
for index, number in enumerate([1, 2, 3], 0):
    pass

if "y" in "python":
    pass

var = "python" if 1 else "PYTHON"
var = "python" if 2 else "PYTHON"
var = "python" if 3 else "PYTHON"

var = "python" if 0 else "PYTHON"
var = "python" if False else "PYTHON"

dictionary = {"a": 1, "b": 2, "c": 3}
dictionary["d"] = 4
del dictionary["d"]
dictionary.clear()
del dictionary

_list = ["p", "y", "t", "h", "o", "n"]

_list.extend(range(3))
_list.extend([3, 4, 5])
_list.extend((6, 7, 8))
_list.extend("python")

_list.insert(0, "!")
_list.append("!")
_list.pop(0)
_list.remove("y")
_list.clear()
del _list

_list = ["aa", "a", "aaaaaa", "aaaa", "aaaaa", "aaa"]
_list.sort(key=lambda x: len(x), reverse=True)

split_one = "the python".split(" ")
split_two = "the<-->python".split(">>>")
# 返回的类型为list
" ".join(split_one)
"<-->".join(split_two)
# 返回的类型为str

"python".ljust(10, " ")
"编程".ljust(8, " ")

if __name__ == "main":
    pass

# _range = range(1, 4)
# _tuple = (1, 2, 3)
# _list = [1, 2, 3]
# _dict = {"left": 1, "middle": 2, "right": 3}

# print(_range, type(_range), _range[0], len(_range))
# print(_tuple, type(_tuple), _tuple[0], len(_tuple))
# print(_list, type(_list), _list[0], len(_list))
# print(_dict, type(_dict), _dict["middle"], len(_dict))

# for i in _dict:
# print(i)
# for i in _dict.keys():
# print(i)
# for i in _dict.values():
# print(i)
# for i, j in _dict.items():
# print(i + ":" + str(j))

print(*"python")
print(*range(3))

_tuple = ("a", "b", "c")
print(_tuple)
print(*_tuple)

_list = ["a", "b", "c"]
print(_list)
print(*_list)

_dict = {"a": 1, "b": 2, "c": 3}
print(_dict)
print(_dict.keys())
print(_dict.values())
print(_dict.items())

print(*_dict)
print(*_dict.keys())
print(*_dict.values())
print(*_dict.items())

_tuple = (1, 2, 3, 4, 5)
_list = [1, 2, 3, 4, 5]
a, b, c, d, e = _tuple
a, b, c, d, e = _list
_list_copy = _list[:]
_list[0:3] = [0]
_list[0:3] = [0, 0]
_list[0:3] = [0, 0, 0]

print(print)
print(range)
print(list)
print(dict)

print(print.__doc__)
print(print.__name__)
# print(print.__code__)

if "i" in "python":
    print("yes")
else:
    print("no")

name = "python"
print(">>>" + name + "<<<")
print(">>>" , name , "<<<")
print(">>>" + name , "<<<")
print(">>>" , name + "<<<")
