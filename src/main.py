class World():
    def __init__(self):
        self.year = 0
        self.month = 0
    
    def pass_time(self):
        if self.month < 12:
            self.month += 1
        else:
            self.year +=1
            self.month = 1

world = World()

class Player():
    def __init__(self, name, realm_index, age):
        self.name = name
        self.realm_index = realm_index
        self.age = age

        self.stats = {
            'qi': 0,
            'health': 100
        }
    

protagonist = Player('Yang Kai', 1, 19)



def cultivate(player):
    player.stats['qi'] += 5

def rest(player):
    player.stats['health'] += 15

def explore(player):
    print('WIP :tongue:')

def breakthrough(player):
    player.realm_index += 1
    player.stats['qi'] = 0



realms = {
    1: {
        'name': 'Qi refining',
        'qi_requirement': 50,
    },
    2: {
        'name': 'Foundation establishment',
        'qi_requirement': 75,
    },
    3: {
        'name': 'Core formation',
        'qi_requirement': 100,
    },
    4: {
        'name': 'Nascent soul',
        'qi_requirement': 125,
    }    
}

actions = {
    'cultivate': cultivate,
    'rest': rest,
    'explore': explore,
    'breakthrough': breakthrough
}



def compile_available_actions(player):
    available_actions = {
        '1': 'cultivate',
        '2': 'rest',
        '3': 'explore'
    }
    
    realm_index = player.realm_index
    qi_requirement = realms[realm_index]['qi_requirement']


    if player.stats['qi'] >= qi_requirement:
        action_number = str(len(available_actions) + 1)
        available_actions[action_number] = 'breakthrough'
    
    return available_actions

def display_available_actions(available_actions):
    print('It is currently year', world.year, 'month', world.month)
    for action_index in available_actions:
        print('['+ action_index + ']', available_actions[action_index])

def check_user_input(user_input, available_actions):
    whitelist = []
    for action_index in available_actions:
        whitelist.append(action_index)
    if user_input in whitelist:
        return True
    else:
        return False

def execute_action(user_input, available_actions, player):
    action = available_actions[user_input]
    actions[action](player)



while True:
    available_actions = compile_available_actions(protagonist)
    display_available_actions(available_actions)
    user_input = input()

    if check_user_input(user_input, available_actions) == False:
        print('Not an option bud')
        continue
    
    execute_action(user_input, available_actions, protagonist)
    world.pass_time()
    
