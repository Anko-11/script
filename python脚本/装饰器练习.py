import time
user = {"root": "123456", "admin": "admin123"}


def deco(username, passwd):
    def runtime(func):
        def inner(*args, **kwargs):
            if username in user and passwd == user[username]:
                print("用户名密码正确")
                if username == "root":
                    start = time.time()
                    result = func(*args, **kwargs)
                    end = time.time()
                    print(f"{func.__name__}执行花了{end - start}")
                    return result
                else:
                    print("用户没有权限")
                    return
            else:
                print("用户名密码不正确")
                return
        return inner
    return runtime


class A:
    def __init__(self, username, passwd):
        self.username = username
        self.passwd = passwd

    def __call__(self, func):
        def inner(*args, **kwargs):
            if self.username in user and self.passwd == user[self.username]:
                print("用户名密码正确")
                if self.username == "root":
                    start = time.time()
                    result = func(*args, **kwargs)
                    end = time.time()
                    print(f"{func.__name__}执行花了{end - start}")
                    return result
                else:
                    print("用户没有权限")
                    return
            else:
                print("用户名密码不正确")
                return
        return inner


# @deco(username="root", passwd="123456")
# @deco(username="admin", passwd="admin123")
@A(username="root", passwd="123456")
# @A(username="admin", passwd="admin123")
def add(a, b):
    time.sleep(1)
    return a + b


add(1, 2)