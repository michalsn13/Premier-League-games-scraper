class Queries:
    TABLE_POINTS="""
    select team, sum(games_played) as games_played, sum(points) as points, sum(goals_scored) as goals_scored, sum(goals_conceded) as goals_conceded, (sum(goals_scored)-sum(goals_conceded)) as goal_difference from
(
select 
home_team as team, count(away_team) as games_played, 
sum(case when substring(ftscore,1,1)>substring(ftscore,3,1) then 3 else 
		(case when substring(ftscore,1,1)<substring(ftscore,3,1) then 0 else 1 end)
	end) as points, 
sum(cast(substring(ftscore,1,1) as int)) as goals_scored, sum(cast(substring(ftscore,3,1) as int)) as goals_conceded 
from premierleague where ftscore!=':'
group by home_team
UNION ALL
select 
away_team as team, count(home_team) as games_played, 
sum(case when substring(ftscore,1,1)<substring(ftscore,3,1) then 3 else 
		(case when substring(ftscore,1,1)>substring(ftscore,3,1) then 0 else 1 end)
	end) as points, 
sum(cast(substring(ftscore,3,1) as int)) as goals_scored, sum(cast(substring(ftscore,1,1) as int)) as goals_conceded 
from premierleague where ftscore!=':'
group by away_team
) as foo
group by team
order by points desc
"""
    TEAMS="""
            SELECT DISTINCT team FROM (
            (SELECT home_team as team from PremierLeague)
            UNION ALL
            (SELECT away_team as team from PremierLeague)
            ) AS FOO
            """