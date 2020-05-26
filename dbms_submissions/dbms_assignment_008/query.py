Q1 = "select d.id,d.fname 
      from director as d 
      where exists(
      select * from movie as m 
      inner join  moviedirector as md on m.id==md.mid where d.id ==md.did and year >2000) and not exists (select * from movie as m inner join  moviedirector as md on m.id==md.mid where d.id ==md.did and year <2000) order by d.id"




Q2 = "select fname ,
     (select name 
     from movie as m 
     inner join 
     moviedirector as md 
     on m.id ==md.mid  
     where md.did =d.id 
     order by rank desc 
     limit 1 )
     from director as d 
     limit 100;"


Q3 = '''select a.id,a.fname,a.lname,a.gender 
        from actor as a
        where not exists(
        select * from cast as c
        inner join  movie as m 
        on m.id==c.mid 
        where a.id==c.pid and year between 1990 and 2000) 
        order by a.id desc limit 100;'''


