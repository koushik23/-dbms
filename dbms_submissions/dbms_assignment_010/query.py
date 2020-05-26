Q1 ='''
    select p.player_id,p.team_id,p.jersey_no,p.name,p.date_of_birth,p.age from 
    player as p 
    inner join 
    matchcaptain as m 
    on p.player_id ==m.captain
    where p.player_id 
    not in 
    (select player_id from goaldetails)
    order by match_no;
   '''
   
   
Q2 ='''
    select team_id,count(match_no)
    from matchteamdetails
    group by team_id;
    '''
    

Q3 = '''
    select team_id,(count(goal_id)+0.0)/(select count(player_id) from player as p where p.team_id=gd.team_id)
    from goaldetails as gd
    group by team_id;
    '''

Q3 = '''
    select team_id,(sum(goal_score)+0.0)/23 as c
    from matchteamdetails as gd
    group by team_id having c >0
    '''    


    
Q4 = '''
    select captain ,count(captain)
    from matchcaptain
    group by captain;
    '''
    
Q5 = '''
    select count(distinct captain)
    from matchcaptain as mc 
    inner join
    match as m
    on mc.captain==m.player_of_match and mc.match_no==m.match_no
    '''
    

Q6 = '''
    select distinct(captain)
    from matchcaptain as mc
    where mc.captain
    not in (
    select player_of_match from match
    );
    '''
    
Q7 = '''
     select strftime('%m',play_date) as month ,
     count(match_no) from match group by month; 
     '''
    
Q8 = '''
    select jersey_no,count(player_id) as c
    from
    matchcaptain as mc inner join player as p 
    on p.player_id==mc.captain
    group by jersey_no
    order by c desc,jersey_no desc;
    '''
Q9 = "select p.player_id, (SELECT avg(audience) from match as m inner join matchteamdetails as mtd on m.match_no==mtd.match_no WHERE mtd.team_id==p.team_id group by team_id) as avg_a from player as p order by avg_a desc,p.player_id desc;"

    
Q10 = '''
     select team_id,avg(age)
     from player
     group by team_id;
     '''
 
 
Q11 ='''
    select avg(age)
    from
    matchcaptain as mc inner join player as p 
    on p.player_id==mc.captain
    '''
    
    
Q12 = "select strftime('%m',date_of_birth) as month ,count(player_id) as c from player group by month order by c desc,month desc ;"



Q13 = "select captain,count(win_lose) as c from matchcaptain as mc inner join matchteamdetails mtd on mc.match_no==mtd.match_no and mc.team_id==mtd.team_id where win_lose= 'W'  group by captain order by c desc"
