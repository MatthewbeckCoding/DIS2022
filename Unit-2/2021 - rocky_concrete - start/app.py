from flask import Flask, render_template, url_for, request, redirect
import sqlite3
import os

app = Flask(__name__)

#connect to the database
con = sqlite3.connect("rockyconcrete.db", check_same_thread=False)
con.row_factory = sqlite3.Row

#create a cursor/pointer to navigate the database
cur = con.cursor()

@app.route('/')
@app.route('/index')
def index():
    sql = """
            select * from customers
            order by cust_name asc;"""
    cur.execute(sql)
    results = cur.fetchall()

    return render_template("index.html", customers=results, title="Customer List")

@app.route('/customer_details', methods=['GET'])
def customer_details():
    if request.args.get('cid'):
        id = int(request.args.get('cid'))

        sql = """
                select *
                from customers
                where cust_no = ?"""
        cur.execute(sql,(id,))
        customer_results = cur.fetchone()

        sql = """
                select count(distinct o.order_no) as 'order count', max(order_date) as 'last order', sum(order_qty * order_price) as 'total orders'
                from orders o, order_details od
                where o. order_no = od.order_no
                and cust_no = ?;"""

        cur.execute(sql,(id,))
        order_count = cur.fetchone()

        sql = """
                select *
                from orders
                where cust_no = ?;"""

        cur.execute(sql,(id,))
        order_hist = cur.fetchall()

        return render_template("customer_details.html", title="Customer Details", cdetails=customer_results, \
                               ocount=order_count, ohist=order_hist)
    else:
        return redirect(url_for("index"))

@app.route('/order_details')
def order_details():
    if request.args.get('oid'):
        id = int(request.args.get('oid'))

        sql = """
                select od.prod_code, order_date, od.order_no, order_qty, order_price, description, order_qty*order_price as 'total' 
                from order_details od, products p, orders o  
                where od.prod_code = p.prod_code
                and o.order_no = od.order_no
                and od.order_no = ?;"""

        cur.execute(sql,(id,))
        order_results = cur.fetchall()

        sql = """
                select sum(order_qty*order_price) as 'order total'
                from order_details
                where order_no = ?;"""

        cur.execute(sql,(id,))
        total = cur.fetchone()

        return render_template("order_details.html", title='Order Details', details=order_results, order_total=total)



if __name__ == '__main__':
    host = '127.0.0.1'
    port = 8000
    app.run(host,port,debug=True)