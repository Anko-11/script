import pickle

normal_goods = {"F001": {"商品": "苹果", "单价": 1, "数量": 1},
                "F002": {"商品": "香蕉", "单价": 1, "数量": 1},
                "F003": {"商品": "雨伞", "单价": 5, "数量": 1},
                "F004": {"商品": "棒球", "单价": 2, "数量": 1},
                "F005": {"商品": "电池", "单价": 3, "数量": 1},
                "F006": {"商品": "水瓶", "单价": 4, "数量": 1}
}
medicine_goods = {
    "M0001": {"商品": "奥司他韦", "单价": 60, "数量": 1},
    "M0002": {"商品": "抗病毒口服液", "单价": 30, "数量": 1}
}

total = 0


class SanleShop:
    def __init__(self, goods, sys_info):
        self.goods = goods
        self.sys_info = sys_info
        self.userdict = {}

    def register(self, name, passwd, balance):
        if name not in self.userdict:
            user = USER(name, passwd, balance)
            self.userdict[name] = user
            file_name = self.sys_info + "_user.pickle"
            with open(file_name, "wb") as fp:
                pickle.dump(self.userdict, fp)
        else:
            print("用户已存在")

    def load_user(self):
        file_name = self.sys_info + "_user.pickle"
        try:
            with open(file_name, "rb") as fp:
                self.userdict = pickle.load(fp)
        except():
            pass

    def login(self, name, passwd):
        if name in self.userdict and passwd == self.userdict[name].passwd:
            return True


class USER:
    def __init__(self, name, passwd, balance):
        self.name = name
        self.passwd = passwd
        self.balance = int(balance)
        self.shopping_cart = {}

    def cart(self, total):
        while 1:
            buy = input("输入商品编号以添加至购物车(q退出)：")
            if buy == "q":
                return total
            else:
                try:
                    if buy not in user.shopping_cart:
                        user.shopping_cart[buy] = system[c1].goods[buy]
                    else:
                        user.shopping_cart[buy]["数量"] += 1
                    for i in user.shopping_cart:
                        print("购买了", user.shopping_cart[i]["商品"], f'{user.shopping_cart[i]["数量"]}个')
                    total += user.shopping_cart[buy]["单价"]
                    print(f'总价{total}价')
                except:
                    print("没有这个商品编号")



system1 = SanleShop(normal_goods, "普通购物系统")
system2 = SanleShop(medicine_goods, "药店购物系统")
system = [system1, system2]

while 1:
    print("当前平台购物系统：")
    for i, j in enumerate(system):
        print(f"{i}.{j.sys_info}")
    c1 = input("输入：（q退出）")
    if c1 == "q":
        break
    if c1.isdigit() and int(c1) < len(system):
        c1 = int(c1)
        system[c1].load_user()
        print(f"欢迎进入{system[c1].sys_info}".center(40, "="))
        c2 = input("1.登录\n2.注册\n输入选择（q退出）")
        if c2 == "q":
            break
        if c2 == "1":
            name, passwd = input("请输入用户名，密码（空白分割）：").split()
            if system[c1].login(name, passwd):
                while 1:
                    c3 = input("1.查看商品\n2.添加购物车\n3.结算购物车\n4.退出\n请输入：")
                    user = system[c1].userdict[name]
                    if c3 == "1":
                        for i in system[c1].goods:
                            print(i, system[c1].goods[i]["商品"], system[c1].goods[i]["单价"], "元")
                    if c3 == "2":
                        total = user.cart(total)
                    if c3 == "3":
                        user.balance -= total
                        print("谢谢惠顾，您的余额为：", user.balance)
                        # file_name = system[c1].sys_info + "_user.pickle"
                        # with open(file_name, "wb") as fp:
                        #     pickle.dump(user.userdict, fp)
                    if c3 == "4":
                        break
            else:
                print("登录失败，请重新登录")
        if c2 == "2":
            name, passwd, balance = input("请输入名字、密码、余额（空白分割）").split()
            system[c1].register(name, passwd, balance)
            print(f"当前用户有：{system[c1].userdict}")
        else:
            print("输入有误")
    else:
        print("输入错误")
