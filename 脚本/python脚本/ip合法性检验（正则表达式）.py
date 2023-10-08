import re
ip = input("输入ip：")
parts = ip.split('.')
if re.match(r"^(\d{1,3}\.){3}\d{1,3}$", ip) and all(0 <= int(part) <= 255 for part in parts):
    print("合法ip")
else:
    print("不合法ip")