class Team:
    '''
    team has a single manager
    team has many players
    team has rankings in a league
    team plays against other teams
    '''
    def __init__(self, name):
            self.name = name
            self.players = []
            
            self.wins = 0
            self.losses = 0

class Game:
    '''
    plays a game bw two teams
    game belongs to a team
    '''
    pass

class League:
    '''
    league has many teams
    each team is going to have a ranking within the league ''' 
    def __init__(self, name): 
        self.name = name
        self.teams = []

    def add_teams(self, teams):
        # finish the current season of the league       
        self.teams = teams      

    def play_season(self):
        # play 10 rounds bw our teams
        for i in range(10):
            self.play_round()
            print('Season ends')

    def play_round(self):
        # play a round which is 
        num_teams = len(self.teams)
        num_games = num_teams // 2;
        for game_num in range(num_games):
            game = Game()

