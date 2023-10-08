import redis
import pymysql

s = input("输入查询id")
r = redis.Redis(host='192.168.17.130', port=6379, db=2, decode_responses=True)
db = pymysql.connect(
    host='192.168.17.130',
    user='sc',
    passwd="sc123789",
    database='sc'
)
cursor = db.cursor()
if s in r.keys("*"):
    print(f"学生姓名为：{r.hget(s, 'name')}")
    print(f"学生年龄为：{r.hget(s, 'age')}")
    print(f"学生地址为：{r.hget(s, 'address')}")
else:
    if cursor.execute("select * from StuInfo where id = ('%s')"%(s)):
        data = cursor.fetchone()
        print(f"学生姓名为{data[1]}")
        print(f"学生年龄为{data[2]}")
        print(f"学生地址为{data[3]}")
        print("id在mysql里并已添加至redis")
        r.hset(s, "name", data[1])
        r.hset(s, "age", data[2])
        r.hset(s, "address", data[3])
    else:
        print("没有这个id")