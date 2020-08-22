from math import pi
from datetime import datetime

dt = datetime.now()
print(f"时间：{dt.year}年{dt.month}月{dt.day}日 {dt.hour}:{dt.minute}:{dt.second}")
print(dt.strftime("%Y年%m月%d日 %H时%M分%S秒 %A"))
