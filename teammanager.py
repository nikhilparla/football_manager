class Team_Manager:
    '''
        runs a team
    '''
    def __init__(self, team):
	self.team = team
	print(' You are a manager')
	print(' You manage ', team.name)
	#print(' You manage {}'.format(self.team))
	print('Good Luck')
