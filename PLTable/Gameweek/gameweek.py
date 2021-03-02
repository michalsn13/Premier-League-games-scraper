import requests
from .gameweek_locators import Gameweek_locators
from Game.game import Game
from bs4 import BeautifulSoup
class Gameweek:
    def __init__(self,number:int):
        if number>38 or number<1:
            raise Exception('No such gameweek.')
        self.number=number
    def __repr__(self):
        return f'Gameweek {self.number}'
    @property
    def games(self):
        code = requests.get(f'https://www.worldfootball.net/schedule/eng-premier-league-2020-2021-spieltag/{self.number}/')
        soup = BeautifulSoup(code.text, 'html.parser')
        rawgames = soup.select_one(Gameweek_locators.TABLE)
        return [Game(i,self.number) for i in rawgames.select(Gameweek_locators.SEPARATOR)]
