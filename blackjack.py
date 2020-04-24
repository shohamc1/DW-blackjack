from libdw import sm
from random import randint, seed
import time

class bjsm (sm.SM):
    start_state = 'ok'

    def get_next_values(self, state, num):
        if num == 21:
            state = 'blackjack'
        elif num > 21:
            state = 'bust'
        else:
            state = state
        
        return state

def PlayAgain():
    # play again loop
    i = input('Play again? (Y/n)')
    
    if i.lower() == 'y':
        return 1
    elif i.lower() == 'n':
        return 0
    else:
        print('Wrong input recieved')
        PlayAgain()
    
    return 'ERROR'

class AI(bjsm):
    def __init__ (self):
        self.num = 0
        self.hand = []
        self.standstate = False
        self.start()
    
    def hit(self):
        new = randint(1, 11)
        self.num += new
        if new == 11:
            self.hand.append('A')
        else:
            self.hand.append(new)
    
    def decide(self):
        if self.standstate == False and (self.getnext() != 'bust' or self.getnext() != 'blackjack'):
            prob = (21 - self.num)/0.11
            roll = randint(0, 100)

            if roll < prob:
                self.hit()
            else:
                self.standstate = True
        else:
            pass
    
    def getnext(self):
        return self.get_next_values(self.state, self.num)

class Player(bjsm):
    def __init__ (self):
        self.num = 0
        self.hand = []
        self.start()


if __name__ == "__main__":
    # initalise variables
    inp = ''

    #instantiate player and AI classes
    ai = AI()
    player = Player()

    # ask for options
    while True:
        seed(time.time())
        inp = input('You hand is {}, for a total of {}\n1. Hit\n2. Stand\n'.format(player.hand, player.num))
        inp = int(inp)

        if inp == 1:
            # hit code
            new = randint(1, 11)
            player.num += new
            if new == 11:
                player.hand.append('A')
            else:
                player.hand.append(new)

            # check if player bust/blackjack
            if player.get_next_values(player.state, player.num) == 'bust':
                print('Busted! You lose :(\n{} for a total of {}.'.format(player.hand, player.num))
                print('AI had {} for a total of {}'.format(ai.hand, ai.num))
                if PlayAgain() == 1:
                    player = Player()
                    ai = AI()
                    pass
                else:
                    break
            
            elif player.get_next_values(player.state, player.num) == 'blackjack':
                print('Blackjack! You win!')
                print('You had {} for a total of {}.'.format(player.hand, player.num))
                print('AI had {} for a total of {}'.format(ai.hand, ai.num))
                if PlayAgain() == 1:
                    player = Player()
                    ai = AI()
                    pass
                else:
                    break
            
            else:
                pass
            # all checks pass

            # AI plays
            ai.decide()

            # check if AI bust/blackjack
            if ai.getnext() == 'bust':
                print('You win!')
                print('You had {} for a total of {}.'.format(player.hand, player.num))
                print('AI had {} for a total of {}'.format(ai.hand, ai.num))
                if PlayAgain() == 1:
                    player = Player()
                    ai = AI()
                    pass
                else:
                    break
            elif ai.getnext() == 'blackjack':
                print ('AI blackjack! You lose :(')
                print('You had {} for a total of {}.'.format(player.hand, player.num))
                print('AI had {} for a total of {}'.format(ai.hand, ai.num))
                if PlayAgain() == 1:
                    player = Player()
                    ai = AI()
                    pass
                else:
                    break
                # all checks pass, loop
        elif inp == 2:
            #stand code

            # AI plays until it stands
            while ai.standstate != True:
                ai.decide()
                
            # check if AI bust/blackjack
            if ai.getnext() == 'bust':
                print('You win! AI busted.')
                print('You had {} for a total of {}.'.format(player.hand, player.num))
                print('AI had {} for a total of {}'.format(ai.hand, ai.num))
                if PlayAgain() == 1:
                    player = Player()
                    ai = AI()
                    pass
                else:
                    break
            elif ai.getnext() == 'blackjack':
                print ('AI blackjack! You lose :(')
                print('You had {} for a total of {}.'.format(player.hand, player.num))
                print('AI had {} for a total of {}'.format(ai.hand, ai.num))
                if PlayAgain() == 1:
                    player = Player()
                    ai = AI()
                    pass
                else:
                    break
            # all checks pass

            
            # check for win/loss conditions
            elif ai.num > player.num:
                print('AI wins! You lose :(')
                print('You had {} for a total of {}.'.format(player.hand, player.num))
                print('AI had {} for a total of {}'.format(ai.hand, ai.num))
                if PlayAgain() == 1:
                    player = Player()
                    ai = AI()
                    pass
                else:
                    break
            elif ai.num < player.num:
                print('You win!')
                print('You had {} for a total of {}.'.format(player.hand, player.num))
                print('AI had {} for a total of {}'.format(ai.hand, ai.num))
                if PlayAgain() == 1:
                    player = Player()
                    ai = AI()
                    pass
                else:
                    break
            else:
                print('It\'s a tie!')
                print('You had {} for a total of {}.'.format(player.hand, player.num))
                print('AI had {} for a total of {}'.format(ai.hand, ai.num))
                if PlayAgain() == 1:
                    player = Player()
                    ai = AI()
                    pass
                else:
                    break
                
        else:
            print('Wrong input recieved!')

    #end
    print('''
    .___________. __    __       ___      .__   __.  __  ___   ____    ____  ______    __    __  
    |           ||  |  |  |     /   \     |  \ |  | |  |/  /   \   \  /   / /  __  \  |  |  |  | 
    `---|  |----`|  |__|  |    /  ^  \    |   \|  | |  '  /     \   \/   / |  |  |  | |  |  |  | 
        |  |     |   __   |   /  /_\  \   |  . `  | |    <       \_    _/  |  |  |  | |  |  |  | 
        |  |     |  |  |  |  /  _____  \  |  |\   | |  .  \        |  |    |  `--'  | |  `--'  | 
        |__|     |__|  |__| /__/     \__\ |__| \__| |__|\__\       |__|     \______/   \______/  ''')                                       