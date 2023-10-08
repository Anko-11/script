class ATM:
    country = "中国"

    def __init__(self, bank, area, balance):
        self.bank = bank
        self.area = area
        self.balance = balance

    def store(self, user, money):
        self.balance += money
        user.balance += money
        print(f"已存入{money}, {user.name}账户余额为：{user.balance}")

    def wd(self, user, money):
        if user.balance >= money:
            self.balance -= money
            user.balance -= money
            print(f"已取出{money}, {user.name}账户余额为：{user.balance}")
        else:
            print("余额不足")

class USER:
    def __init__(self, balance, name, passwd):
        self.balance = balance
        self.name = name
        self.passwd = passwd


atm1 = ATM("中国农业银行", "长沙", 2000)
user1 = USER(200, "赵", "123456")
atm1.store(user1, 1000)
atm1.wd(user1, 1200)
