# coding:utf-8
import pymysql

# 关于中文问题
# 1. mysql命令行创建数据库，设置编码为gbk：create databse demo2 character set utf8;
# 2. python代码中连接时设置charset="gbk"
# 3. 创建表格时设置default charset=utf8
sql_conf = {
    'test': {
        'host': '192.168.1.3',
        'user': "root",
        'password': "&Testbtc38&..",
        'charset': "utf8",
        'port': 3306
    },
    'swap': {
        'host': "192.168.1.7",
        'user': "aexdev",
        'password': "&Testbtc38&..",
        'charset': "utf8",
        'port': 3306
    }
}


class Mysql:  # 单例模式
    __conn = None

    def __init__(self):
        pass

    @staticmethod
    def get_instance(database, db):
        if Mysql.__conn is None:
            # 连接数据库
            Mysql.__conn = pymysql.connect(
                host=sql_conf[database]['host'],
                user=sql_conf[database]['user'],
                passwd=sql_conf[database]['password'],
                db=db,
                charset=sql_conf[database]['charset'],
                port=sql_conf[database]['port'])  # 和mysql服务端设置格式一样（还可设置为gbk, gb2312）
        return Mysql

    @staticmethod
    def update(sql):  # 增删改查
        # 创建游标
        cursor = Mysql.__conn.cursor()
        # 执行sql语句,返回受影响的行数
        row = cursor.execute(sql)
        # 提交
        Mysql.__conn.commit()
        # 关闭游标
        cursor.close()
        # 关闭连接
        Mysql.__conn.close()
        return row

    @staticmethod
    def select(select_sql, is_dict=False):  # 增删改查
        # 创建游标
        if is_dict:
            cursor = Mysql.__conn.cursor(cursor=pymysql.cursors.DictCursor)
        else:
            cursor = Mysql.__conn.cursor()
        cursor.execute(select_sql)
        ret = cursor.fetchall()  # 获取所有数据，获取后游标会向下移动到末尾
        return ret
