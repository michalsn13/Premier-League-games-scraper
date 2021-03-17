import psycopg2.errors
import asyncio
from time import time
import plotly.graph_objects as pgo
from .pltable_queries import Queries
from Connection.connection import Connection
from Gameweek.gameweek import Gameweek
from Connection.async_con import Async_con
class PLTable:
    @classmethod
    def new_table(self):
        with Connection() as con:
            cursor=con.cursor()
            cursor.execute('DROP TABLE IF EXISTS PremierLeague CASCADE')
        with Connection() as con:
            cursor=con.cursor()
            cursor.execute("CREATE TABLE PremierLeague(GAMEWEEK INT, GAMEDATE DATE,GAMETIME TIME, HOME_TEAM TEXT, AWAY_TEAM TEXT,FTSCORE TEXT,HTSCORE TEXT,PRIMARY KEY (HOME_TEAM,AWAY_TEAM))")
    @classmethod
    def add_game(self,game):
            try:
                with Connection() as con:
                    cursor = con.cursor()
                    cursor.execute(f"INSERT INTO PremierLeague VALUES({game.gw},'{game.date}','{game.time}','{game.home_team}','{game.away_team}','{game.score[0]}','{game.score[1]}')")
            except psycopg2.errors.UniqueViolation:
                with Connection() as con:
                    cursor = con.cursor()
                    cursor.execute(f"UPDATE PremierLeague SET GAMEWEEK={game.gw},GAMEDATE='{game.date}',GAMETIME='{game.time}', FTSCORE='{game.score[0]}',HTSCORE='{game.score[1]}' WHERE HOME_TEAM='{game.home_team}' AND AWAY_TEAM='{game.away_team}'")
            except IndentationError:
                print('Table does not exist, creating one.')
                self.new_table()
                self.add_game(game)
    @classmethod
    def update_table(self):
        t0=time()
        async_con=Async_con()
        pages=[f'https://www.worldfootball.net/schedule/eng-premier-league-2020-2021-spieltag/{i}/' for i in range(1,39)]
        for games in [Gameweek(i+1,j).games for i,j in enumerate(async_con.loop.run_until_complete(async_con.get_multiple_pages(*pages)))]:
            for game in games:
                self.add_game(game)
        print(time()-t0)
    @classmethod
    def show_table(self):
        with Connection() as con:
            cursor=con.cursor()
            try:
                cursor.execute(Queries.TABLE_POINTS)
            except IndentationError:
                print('No such table. Create one first.')
            else:
                rows=cursor.fetchall()
                fig = pgo.Figure(data=[pgo.Table(
                    header=dict(values=['Place','Team','Games played','Points','Goals scored','Goals conceded','Goal difference']
                                , fill_color='paleturquoise',
                                align='left'
                                ),
                    cells=dict(values=[list(range(1,len(rows)+1))]+[[i[k] for i in rows] for k in range(6)]
                               , fill_color='lavender',
                               align='left'
                               ))
                ])
                fig.show()
    @classmethod
    def teams(cls):
        with Connection() as con:
            cursor=con.cursor()
            cursor.execute(Queries.TEAMS)
            teams=cursor.fetchall()
            result=sorted([game[0] for game in teams])
            for team in result:
                print(team)
            return result
    @classmethod
    def team_fixture(self):
        club=input('Enter valid team: ')
        with Connection() as con:
            cursor=con.cursor()
            cursor.execute(f"""
            SELECT * FROM PremierLeague
            WHERE (home_team='{club}' OR away_team='{club}') AND ftscore=':'
            ORDER BY gamedate ASC""")
            x=cursor.fetchall()
            if x==[]:
                print('No games.')
            else:
                for game in x:
                    print(f'GW{game[0]} <{game[1]} {game[2]}> {game[3]} vs {game[4]}')
    @classmethod
    def team_results(self):
        club = input('Enter valid team: ')
        with Connection() as con:
            cursor=con.cursor()
            cursor.execute(f"""
            SELECT * FROM PremierLeague
            WHERE (home_team='{club}' OR away_team='{club}') AND ftscore!=':'
            ORDER BY gamedate ASC""")
            x=cursor.fetchall()
            if x==[]:
                print('No games.')
            else:
                for game in x:
                    print(f'GW{game[0]} <{game[1]} {game[2]}> {game[3]} {game[5]} ({game[6]}) {game[4]}')
