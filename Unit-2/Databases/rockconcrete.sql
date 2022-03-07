/*SQ1*/
select cust_name
from customers;

/*SQ2*/
select description, list_price
from products;

/*SQ3*/
select *
from customers;

/*SQ4*/
select *
from products
where list_price > 100;

/*SQ5*/
select cust_name, curr_bal
from customers
where curr_bal > 250;

/*SQ6*/
select *
from products
where prod_group = 'A';

/*SQ7*/
select *
from products
where qty_on_hand * list_price > 1000;

/*SQ8*/
select cust_no, cust_name as 'name', cr_limit, curr_bal * 0.9 as 'reduced balance'
from customers
where curr_bal > cr_limit;

/*SQ9*/
select *
from customers
where post_code > 4000 and post_code < 5000;

/*SQ10*/
select prod_code, description, remake_qty
from products
where qty_on_hand < remake_level;



