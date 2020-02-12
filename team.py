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

class Manager:
'''
	runs a team
'''
	pass

class Player:
	'''
	player is on a single team , with many other players
	player plays in a game for a team
	'''
	def __init__(self, name):
	self.name = name

	# players skill rating
	pass

	# salary
	pass	

class League:
	'''
	league has many teams
	each team is going to have a ranking within the league
	'''
	def __init__(self, name):
		self.name = name
		self.teams = []

	def add_teams(self, teams):
		# finish the current season of the league	
		self.teams = teams	

class Game:
	'''
	plays a game bw two teams
	game belongs to a team
	'''
	pass
