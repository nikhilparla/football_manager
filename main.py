#! /usr/bin/python

from team import League, Team

def main():
	''' set up the data '''
	# we have a single league
	first_league = League('Premiership League')
    
    # set up the teams
    teams = [
        Team('chelsea'),
        Team('Man City'),
        Team('Hull City'),
        Team( 'West Hamy'),
        Team('Arsenal')
    ]
    
    # generate some players
    for i in range(100):
        players.append(generate_player())    
        


if __name__ == '__main__':
	main()
