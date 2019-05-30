import mysql.connector


def check_sql(order_id, status):
    db = mysql.connector.connect(host="localhost",    # your host, usually localhost
                         user="myuser",         # your username
                         passwd="password",  # your password
                         db="pizza_deliver_db")        # name of the data base

    cur = db.cursor()

    order_id == cur.execute("SELECT order_id FROM PizzaOrders WHERE order_id = %s")
    status == cur.execute("SELECT status FROM PizzaOrders WHERE order_id = %s")

    db.close()