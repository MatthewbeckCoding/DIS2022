import sqlite3

#connect to database
con = sqlite3.connect("Databases/rockyconcrete.db")

#create a cursor/pointer to navigate the databases
con.row_factory = sqlite3.Row #enables us to use column headings
cur = con.cursor() #pointer to use in the database

# sql = """
#         select *
#         from customers
#         where town = 'Brisbane'; """
#
# cur.execute(sql)
#
# results = cur.fetchall()
#
# print(results)

#parameter query
town = input("enter the down to search for: ")
min_credit = int(input("enter credit limit: "))

sql = """
        select * 
        from customers
        where town like ?
        and cr_limit >= ?;"""

cur.execute(sql,('%'+town+'%',min_credit))

results = cur.fetchall()


if len(results) > 0:
    for row in results:
        print(row['cust_name'], 'lives in', row['street'], 'in', row['town'], 'with a credit limit of', row['cr_limit'])
else:
    print("no records found")









