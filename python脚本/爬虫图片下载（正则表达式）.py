import requests
import os

web = 'https://www.sanchuangedu.cn/'
x = requests.get(web)
picture = re.findall(r"(?<==)\w*.jpg|(?<==)\w*.png", x.text, re.M | re.S)
dir = "sc_pic"
if not os.path.exists(dir):
    os.mkdir(dir)
for i in picture:
    r = requests.get(web + i)
    with open(dir + "/" + i, "wb") as f:
        f.write(r.content)