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
     

     
Q6 = "select distinct(pid) from cast group by mid,pid having count(distinct role)>1 order by pid  limit 100;"  
  
    
Q7 = '''
     select distinct(fname),(select count(fname) from 
     director as d1 where d.fname = d1.fname
     )as c from director as d where c>1 
     '''
   
Q9 = '''select m1.id,
      count(case when gender='F' then 1 end)as no_of_female_actors,
      count(case when gender='M' then 1 end)as no_of_male_actors
      from (select id from movie limit 100) as  m1 
          inner join cast as c1 
          on c1.mid==m1.id 
          inner join actor as a 
          on a.id==c1.pid 
      group by m1.id '''
 
 
Q10 = '''select m1.id
     from (select id from movie limit 100) as  m1 
          inner join cast as c1 
          on c1.mid==m1.id 
          inner join actor as a 
          on a.id==c1.pid 
      group by m1.id having count(case when gender='F' then 1 end)>=1
     count(case when gender='M' then 1 end)>=1 limit 100
     '''
 
     
     

Q8 = '''select distinct(md.did),d.fname,d.lname 
     from 
     moviedirector as md 
     inner join cast as c 
     on md.mid==c.mid 
     inner join director as d 
     on d.id==md.did 
     where md.did 
     not in(
               select md.did 
               from 
                    moviedirector as md 
                    inner join cast as c 
                    on md.mid==c.mid  
                    group by md.did,md.mid 
                    having  count(distinct pid)<100
           ) 
     group by md.did,md.mid 
     having count(distinct pid)>=100;
     '''
     
     
     


