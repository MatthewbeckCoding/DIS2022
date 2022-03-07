import sqlite3

#connect to database
con = sqlite3.connect("Databases/rockyconcrete.db")

#create a cursor/pointer to navigate the databases
con.row_factory = sqlite3.Row #enables us to use column headings
cur = con.cursor() #pointer to use in the database

name= input("enter the down to search for: ")

sql = """
        select , cust_name, cust_no, cr_limit-curr_bal as 'available'
        from customers c, orders o
        where c.cust_no = o.cust_no
        and cust_name like ?;"""


cur.execute(sql,('%'+name+'%',))
results = cur.fetchall()

if len(results) > 0:
    for row in results:

        sql = """
                select max(orer_no) as 'order_no', max(order_date) as 'order_date'
                from orders
                where cust_no = ?"""

        cur.execute(sql, (row['cust_no'],))
        results = cur.fetchall()

        if len(result) = 0:
            result = 'No orders made'
        else:
            result = "last order num" + str(result['order_no'])
        print(row['cust_name'], row['cust_no'], row['curr_bal'], row['available'], row['order_no'])
else:
    print("no records found")