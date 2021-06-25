import sql


class datacenter:
    def __init__(self, table):
        self.conn = sql.Mysql.get_instance('test', 'bitcc_datacenter')
        self.table = table

    def get_instance(self):
        return self


if __name__ == '__main__':
    db = datacenter('t_day_swap_user_balance')
    select_sql = "select * from {table} where {where}".format(table=db.table, where=1)
    ret = db.conn.select(select_sql, True)
    print(ret)
    for _ in ret:
        print(_['issued_quantity'] + 1)