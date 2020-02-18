#! /usr/bin/python

from player import generate_player 
from team import League, Team
from teammanager import Team_Manager
import random

def main():
    # generate some players
    players = []
    for i in range(100):
        players.append(generate_player())    
    
    # set up the teams
    teams = [Team('chelsea'),Team('Man City'),Team('Hull City'),Team( 'West Hamy'),Team('Arsenal'),Team('Swansea')]


    for team in teams:
        for player_num in range(11):
            # give the team some players
            selected_player = random.choice(players)
            team.players.append(selected_player)
            players.remove(selected_player)
   

    # create a manager
	manager = Team_Manager(random.choice(teams))

    # we have a single league
    first_league = League('Premiership League')
    first_league.add_teams(teams)

    print('season begins ')
    for i in range(10):
        first_league.play_round()
    print('Season ends')

    # print the players and teams and league
    for team in first_league.teams:
        print(team.name)
        for player in team.players:
            print(player.name),
        print("\n")


if __name__ == '__main__':
        main()
