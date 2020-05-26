Q1 = '''select distinct(a.id),a.fname,a.lname,a.gender
     from actor as a
     inner join cast as c
     on a.id==c.pid 
     inner join movie as m on m.id==c.mid
     where m.name like 'Annie%'
     '''
     
Q2 = '''
     select m.id,m.name,m.rank,m.year
     from movie as m
     inner join moviedirector as md
     on m.id==md.mid
     inner join director d
     on d.id==md.did
     where d.fname='Biff' and d.lname = 'Malibu' and year in(1994,1999,2003)
     order by rank desc ,year;
     '''
     
Q3 = '''
     select
     year ,count(id)
     from movie as m
     group by year
     having avg(rank)>(select avg(rank) from movie)
     '''
     
Q4 = '''
     select 
     m.id,m.name,m.year,m.rank 
     from movie as m
     where year =2001 and rank<(select avg(rank) from movie where year)
     order by rank desc
     limit 10
     '''
     
Q5 = '''
     select 
     m.id,count(gender)
     from movie as m
     inner join cast as c
     on m.id==c.mid
     inner join actor  as a
     on a.id==cast.pid
     where 
     '''
     
     
Q6 = '''
    select distinct(pid)
    from cast
    group by mid
    having count(role)>1
    limit 100
    '''
    
Q7 = '''
     select distinct(fname),(select count(fname) from 
     director as d1 where d.fname = d1.fname
     )as c from director as d where c>1 
     '''
   
   
Q8 = '''
     select d.id,d.fname,d.lname
     from director as d
     inner join moviedirector as md 
     on d.id==md.did
     inner join
     movie as m
     on m.id==md.mid
     inner join 
     cast as c
     on c.mid==m.id
     group by d.id,m.id
     having count(pid)==count(distinct role) or count(distinct role)
     '''
     
     
     