 


Q3 = '''select m1.id as movie_id,
      count(case when gender='M' then 1 end)as no_of_male_actors,
      count(case when gender='F' then 1 end)as no_of_female_actors
      from (select id from movie limit 100) as  m1 
          inner join cast as c1 
          on c1.mid==m1.id 
          inner join actor as a 
          on a.id==c1.pid 
      group by m1.id '''
 
Q2 = "select id as movie_id,m as no_of_male_actors,f as no_of_female_actors from actors" 
 
Q5=''' 
  select distinct(m),c,c1 from 
   (select m.id as m,count(gender)as c from
    (select id from movie limit 100)as m
     inner join cast c on m.id==c.mid
     inner join actor as a on a.id==c.pid
     where gender='F' group by m.id) as c 
  inner join
     (select m.id as n ,count(gender)as c1 from
     (select id from movie limit 100)as m
     inner join cast c on m.id==c.mid
     inner join actor as a on a.id==c.pid
     where gender='M' group by m.id) as d
     on m==n ;
    '''

Q1 = '''select distinct(a.id),a.fname,a.lname,a.gender
     from actor as a
     inner join cast as c
     on a.id==c.pid 
     inner join movie as m on m.id==c.mid
     where m.name like 'Annie%'
     '''

Q5 = '''
      select mid,
       (select count(pid) 
       from cast as c2  
       where pid in 
         (select id from actor where gender='F')
         and 
         c2.mid==c.mid group by mid)as f,            
      
      (select count(pid) from cast as 
      c1 where pid in 
      (select id from actor where gender='M') 
      and 
      c1.mid==c.mid group by mid)as m
      from cast as c
      group by mid
      limit 100;
     '''