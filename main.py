#! /usr/bin/python

from player import generate_player 
from team import League, Team
import random

def main():
    # generate some players
    players = []
    for i in range(100):
        players.append(generate_player())    
    
    # set up the teams
    teams = [Team('chelsea'),Team('Man City'),Team('Hull City'),Team( 'West Hamy'),Team('Arsenal'),]


    for team in teams:
        for player_num in range(11):
            # give the team some players
            selected_player = random.choice(players)
            team.players.append(selected_player)
            players.remove(selected_player)
    
    # we have a single league
    first_league = League('Premiership League')
    first_league.add_teams(teams)




if __name__ == '__main__':
        main()
