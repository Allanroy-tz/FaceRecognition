import pymysql
import pandas as pd


class MysqlHelper:
    db = pymysql.connect(
        host="127.0.0.1",
        port=3302,
        user='Allanroy',  # 在这里输入用户名
        password='Mysql777700',  # 在这里输入密码
        charset='utf8mb4',
        database='faceInfo'
    )
    cursor = db.cursor()  # 创建游标对象

    def FindLabel(self, id):
        sql = 'SELECT label FROM faceinfo.facelabel where id =' + str(id)  # sql语句
        # self.cursor.execute(sql)  #执行sql语句
        result = pd.read_sql(sql, self.db)
        print("查询语句执行成功")
        # one = self.cursor.fetchone()  #获取一条数据
        print("数据获取成功:", result)
        return result

    def InsertLabel(self, id, name):
        sql = 'INSERT INTO faceinfo.facelabel(id, label) VALUES("' + str(id) + '","' + str(name) + '");'
        self.cursor.execute(sql)  # 执行sql语句
        self.db.commit()
        print("插入语句执行成功")


# sql = MysqlHelper()
# label = sql.FindLabel(0).iloc[0].values[0]
# print("-------------------")
# print(label)
