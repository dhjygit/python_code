from datetime import datetime


def run_nian(year):
    return year % 400 == 0 or year % 4 == 0 and year % 100 != 0


# year = int(datetime.now().strftime("%Y"))
year = datetime.now().year

if run_nian(year):
    print(f"{year}是闰年")
else:
    print(f"{year}不是闰年")
