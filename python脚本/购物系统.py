import json

date = {"root": {"passwd": "123456", "balance": 99999}}
database = json.dumps(date)
fp = open("database.txt", "w")
fp.write(database)
fp.close()

# 商品
goods = {"F001": {"商品": "苹果", "单价": 1, "数量": 1},
         "F002": {"商品": "香蕉", "单价": 1, "数量": 1},
         "F003": {"商品": "雨伞", "单价": 5, "数量": 1},
         "F004": {"商品": "棒球", "单价": 2, "数量": 1},
         "F005": {"商品": "电池", "单价": 3, "数量": 1},
         "F006": {"商品": "水瓶", "单价": 4, "数量": 1}
         }


# 登陆系统

def login():
    global data, username
    # 读取账户数据
    fp = open("database.txt")
    database = fp.read()
    fp.close()
    data = json.loads(database)
    if choice == 1:
        username = str(input("用户名："))
        passwd = str(input("密码："))
        for i, j in data.items():
            if i == username and j["passwd"] == passwd:
                print(f"登陆成功,欢迎{username}")
                print(f"余额{j['balance']}")
                return 1
    if choice == 2:
        username = input("注册用户名：")
        passwd = input("注册密码：")
        balance = int(input("注册余额："))
        data[username] = {"passwd": passwd, "balance": balance}
        fp = open("database.txt", "w")
        database = json.dumps(data)
        fp.write(database)
        fp.close()
        login()


# 购物系统
def shopping(cart, total):
    buy = str(input("输入商品编号以添加至购物车,输入0以结算并退出："))
    if buy != "0":
        if buy in cart:
            cart[buy]["数量"] += 1
        else:
            cart[buy] = goods[buy]
        for i in cart:
            print("购买了", cart[i]["商品"], f'{cart[i]["数量"]}个')
            total = cart[i]["单价"] * cart[i]["数量"] + total
        print(f'总价{total}价')
        shopping(cart, total)
    elif data[username]["balance"] < total:
        print("余额不足")
        return 1
    else:
        data[username]["balance"] = data[username]["balance"] - total
        print(data[username]["balance"])
        fp = open("database.txt", "w")
        database = json.dumps(data)
        fp.write(database)
        fp.close()
        return 0


choice = ""
while choice != "exit":
    choice = int(input("欢迎来到Anko购物系统\n输入1登录，输入2注册，exit退出:"))
    if login() == 1:
        total = 0
        cart = {}
        print("F001: 苹果1价。  F002: 香蕉1价。\nF003: 雨伞5价。  F004: 棒球2价。\nF005: 电池3价。  F006: 水1价。")
        shopping(cart, total)
