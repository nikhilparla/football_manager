import random

class Player:
    '''
    player is on a single team , with many other players
    player plays in a game for a team
    '''
    def __init__(self, name, skill):
        self.name = name # players skill rating
    
        self.skill = skill

    # salary
    def salary():
        return 50000 + self.skill * 100

def generate_player():
   first_names = ["Liam", "Noah", "William", "James", "Oliver", "Benjamin", "Elijah", "Lucas", "Mason", "Logan", "Alexander", "Ethan", "Jacob", "Michael", "Daniel", "Henry", "Jackson", "Sebastian", "Aiden", "Matthew", "Samuel", "David", "Joseph", "Carter", "Owen", "Wyatt", "John", "Jack", "Luke", "Jayden", "Dylan", "Grayson", "Levi", "Isaac", "Gabriel", "Julian", "Mateo", "Anthony", "Jaxon", "Lincoln", "Joshua", "Christopher", "Andrew", "Theodore", "Caleb", "Ryan", "Asher", "Nathan", "Thomas", "Leo"]

   first_name = random.choice(first_names)
   last_name = random.choice(first_names)

   full_name = '{} {}'.format(first_name, last_name)

    #generate skill and salary
    skill = 10 + random.randint(90)


    return Player(full_name, skill)
