select name, age, sex
from members
where sex = 'm'
and age > 50
order by name desc;

select age, name, sex, likes
from members
where likes = 'dancing'
order by sex asc, name asc;

select sex, name, likes
from members
where likes = 'politics';

select name, likes, dislikes
from members
where likes = dislikes;

select name, sex, age
from members
where sex = 'f'
and age between 20 and 40;

select name
from members
where name like 'a%';

select name
from members
where name like '_a%'
