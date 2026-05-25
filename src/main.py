class WorldState():
    def __init__(self):
        self.year = 0
        self.month = 0
    
    def pass_time(self):
        if self.month != 12:
            self.month += 1
        else:
            self.year += 1
            self.month = 0
        

class Person():
    def __init__(self, name, age, realm, gender):
        self.name = name
        self.age = age
        self.realm = realm
        self.gender = gender

        self.stats = {
            'qi': 0,
            'health': 100
        }

class Event():
    def __init__(self, title, description, conditions, choices):
        self.title = title
        self.description = description
        self.conditions = conditions
        self.choices = choices

world_state = WorldState()

def display_options(world_state):
    year = world_state.year
    month = world_state.month
    print('It is currently year', year, 'month', month)
    print('[1]. Cultivate')
    print('[2]. Rest')
    print('[3]. Explore')

def check_input(user_input):
    whitelist = ['1', '2', '3']
    if user_input in whitelist:
        return True
    else:
        return False

def cultivate(player):
    player.stats['qi'] += 5
    return player

def rest(player):
    player.stats['health'] += 15
    return player

player = Person('Yang Kai', 19, 'Qi refining', 'Male')



while True:
    display_options(world_state)

    user_input = input()
    if check_input(user_input) == False:
        print('Not an option bud, try again \n')
        user_input = input()
    
    if user_input == '1':
        player = cultivate(player)
        print('Qi is now:', player.stats['qi'])
        world_state.pass_time()
        
    elif user_input == '2':
        player = rest(player)
        print('Health is now:', player.stats['health'])
        world_state.pass_time()

