Q1 = "Select a.fname,a.lname from(actor inner join cast on id == pid)as a where a.mid=12148;"
Q2 = "select count(a.id) from (actor inner join cast on id ==pid)as a where a.fname = 'Harrison (I)' and a.lname = 'Ford';"
Q3 = "select distinct(pid) from (cast inner join movie on id==mid)as a where a.name like 'Young Latin Girls%';"
Q4 = "select count(distinct a.pid) from(movie inner join cast on id = mid) as a where a.year between 1990 and 2000;"