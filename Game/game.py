from .game_locators import Game_locators
class Game:
    def __init__(self,parent,gw):
        self.parent=parent
        self.gw=gw
    def __repr__(self):
        return f'GW{self.gw} <{self.date} {self.time}> {self.home_team} {self.score[0]} ({self.score[1]}) {self.away_team}'
    @property
    def home_team(self)->str:
        return self.parent.select(Game_locators.DETAILS)[0].attrs['title']
    @property
    def away_team(self)->str:
        return self.parent.select(Game_locators.DETAILS)[1].attrs['title']
    @property
    def score(self)->tuple:
        scorer = self.parent.select(Game_locators.DETAILS)[2].string.strip()
        if scorer == "-:-" or scorer == "resch.":
            return (":",":")
        ftscore = scorer[:3]
        htscore = scorer[5:-1]
        return (ftscore,htscore)
    @property
    def date(self)->str:
        game_date=self.parent.select_one(Game_locators.TIME_DETAILS).string
        if not game_date:
            return Game(self.parent.previous_sibling.previous_sibling, self.gw).date
        gd=game_date.split("/")
        return f'{gd[2]}-{gd[1]}-{gd[0]}'
    @property
    def time(self)->str:
        gametime=self.parent.select('td')[1].string
        if not gametime:
            return "00:00:00"
        return f"{self.parent.select('td')[1].string}:00"
