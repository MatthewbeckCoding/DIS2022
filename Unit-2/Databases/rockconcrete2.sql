--Join Queries
select p.prod_code, description, order_price, order_qty
from order_details od, products p 
where od.prod_code = p.prod_code
and order_no = 1234;

select prod_code, description, order_price, order_qty
from order_details od
inner join products p
on od.prod_code = p.prod_code
and order_no = 1234;

--jq2
select cust_name, street, town, post_code, order_date
from customers c, orders o
where c.cust_no = o.cust_no
and order_date like '1706%'
order by order_date asc;

--jq3

select order_no, order_price, prod_code, list_price
from products p, order_details od
where p.prod_code = od.prod_code
and order_price <> list_price;

--jq4
select cust_name, order_date, order_qty * order_price as 'total_price'
from customers c, orders o, order_details od
where c.cust_no = o.cust_no
and o.order_no = od.order_no
and order_qty * order_price > 500
order by order_date asc, total_price desc;

select description, cust_name
from customers c, order_details od, orders o, products p
where c.cust_no = o.cust_no
and o.order_no = od.order_no
and od.prod_code = p.prod_code
and c.town = 'Brisbane';

select cust_name,curr_bal, cr_limit, order_date, order_qty * order_price as 'total'
from customers c, orders o, order_details od
where c.cust_no = od.cust_no
and o.order_no = od.order_no
and curr_bal > cr_limit;

select p.prod_code, o.order_no, o.order_date, order_qty
from orders o, order_details od, products p
where p.prod_code = od.prod_code
and od.order_no = o.order_no
and order_qty > remake_qty;

select cust_name, order_qty, list_price, order_price
from customers c, order_details od, products p, orders o
where c.cust_no = o.cust_no
and o.order_no = od.order_no
and od.prod_code = p.prod_code
and prod_group = 'A'
and post_code like '4%';

