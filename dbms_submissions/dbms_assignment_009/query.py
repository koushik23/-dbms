Q1 = "select avg(age) from player;"

Q2 = '''select match_no,play_date 
    from match 
    where audience>50000 
    order by match_no;'''



Q3 ='''select team_id, count(win_lose) as won 
    from matchteamdetails 
    where win_lose='W' 
    group by team_id 
    order by won desc,team_id;'''
    
    

Q4 ='''select match_no ,play_date 
    from match where stop1_sec>(select avg(stop1_sec) from match) order by match_no desc;'''

Q5 = "select match_no,t.name,p.name from matchcaptain as mc inner join team as t on mc.team_id==t.team_id inner join player as p on p.player_id==mc.captain order by mc.match_no ASC,t.name ASc;"

#Q5 = "SELECT mc.match_no, t.name, p.name FROM (MatchCaptain as mc inner join Team as t ON t.team_id = mc.team_id inner join Player as p ON mc.captain = p.player_id ) ORDER BY mc.match_no ASC,t.name ASC;"



Q6 = "select match_no,name,jersey_no from match inner join player on player_of_match==player_id order by match_no;"

Q7 = "select t.name,avg(age)from team as t inner join player as p on t.team_id==p.team_id group by t.team_id having avg(age)>26;"

#Q8 = "select name,jersey_no,age,count(goal_id) from goaldetails as gd inner join player as p on gd.player_id==p.player_id group by p.player_id having age<=27 and count(goal_id)>0 order by count(goal_id) desc,name;"


Q8 ="SELECT p.name, p.jersey_no, p.age, COUNT(gd.goal_id) as goals FROM Player as p INNER JOIN GoalDetails as gd ON p.player_id = gd.player_id AND p.team_id = gd.team_id AND  p.age <= 27 GROUP BY p.name HAVING COUNT(gd.goal_id) > 0 ORDER BY goals DESC,P.name ASC;"




Q9 = "SELECT t.team_id as id,COUNT(gd.goal_id)*100.0/(SELECT COUNT(*) from goaldetails) FROM team as t INNER JOIN GoalDetails as gd on t.team_id = gd.team_id GROUP BY t.team_id HAVING COUNT(gd.goal_id) > 0;"


Q10 = "select avg (c) from(select count(goal_id) as c from goaldetails group by team_id);"

Q11 = "select player_id,name,date_of_birth from player where player_id not in (select player_id from goaldetails) order by player_id;"

Q12 = "select t.name,m.match_no,m.audience,m.audience-(select avg(m1.audience) from (match as m1 inner join matchteamdetails as mtd1 on m1.match_no==mtd1.match_no) where mtd1.team_id==t.team_id)as difference from match as m inner join matchteamdetails as mtd  on m.match_no==mtd.match_no inner join team as t on t.team_id ==mtd.team_id  order by m.match_no ;"

