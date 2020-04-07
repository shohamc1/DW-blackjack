'''TODO: Add in dealer AI
For dealer AI: calculate probability of going over -> roll d100 -> if over then stand otherwise hit
'''

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

class AI():
    def __init__ (self):
        self.num = 0
        self.hand = []
        self.aistate = bjsm()
        self.standstate = False
        self.aistate.start()
    
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
        return self.aistate.get_next_values(self.aistate.state, num)
        

if __name__ == "__main__":
    # initalise variables
    bjstate = bjsm()
    bjstate.start()
    num = 0
    hand = [] #list of cards
    inp = ''

    ai = AI()

    # ask for options
    while True:
        seed(time.time())
        inp = input('You hand is {}, for a total of {}\n1. Hit\n2. Stand\n'.format(hand, num))
        inp = int(inp)

        if inp == 1:
            # hit code
            new = randint(1, 11)
            num += new
            if new == 11:
                hand.append('A')
            else:
                hand.append(new)

            if bjstate.get_next_values(bjstate.state, num) == 'bust':
                print('Busted! You lose :(\n{} for a total of {}.'.format(hand, num))
                print('AI had {} for a total of {}'.format(ai.hand, ai.num))
                if PlayAgain() == 1:
                    num = 0
                    hand = []
                    bjstate.start()
                    pass
                else:
                    break
            
            elif bjstate.get_next_values(bjstate.state, num) == 'blackjack':
                print('Blackjack! You win!')
                print('You had {} for a total of {}.'.format(hand, num))
                print('AI had {} for a total of {}'.format(ai.hand, ai.num))
                if PlayAgain() == 1:
                    num = 0
                    hand = []
                    bjstate.start()
                    pass
                else:
                    break
            
            else:
                pass

            # AI plays
            ai.decide()

            if ai.getnext == 'bust':
                print('You win!')
                print('You had {} for a total of {}.'.format(hand, num))
                print('AI had {} for a total of {}'.format(ai.hand, ai.num))
                if PlayAgain() == 1:
                    num = 0
                    hand = []
                    bjstate.start()
                    pass
                else:
                    break
            if ai.getnext() == 'blackjack':
                print ('AI blackjack! You lose :(')
                print('You had {} for a total of {}.'.format(hand, num))
                print('AI had {} for a total of {}'.format(ai.hand, ai.num))
                if PlayAgain() == 1:
                    num = 0
                    hand = []
                    bjstate.start()
                    pass
                else:
                    break
        elif inp == 2:
            while ai.standstate != True:
                ai.decide()

                print(ai.num, ai.getnext())
                
                if ai.getnext() == 'bust':
                    print('You win!')
                    print('You had {} for a total of {}.'.format(hand, num))
                    print('AI had {} for a total of {}'.format(ai.hand, ai.num))
                    if PlayAgain() == 1:
                        num = 0
                        hand = []
                        bjstate.start()
                        pass
                    else:
                        break
                if ai.getnext() == 'blackjack':
                    print ('AI blackjack! You lose :(')
                    print('You had {} for a total of {}.'.format(hand, num))
                    print('AI had {} for a total of {}'.format(ai.hand, ai.num))
                    if PlayAgain() == 1:
                        num = 0
                        hand = []
                        bjstate.start()
                        pass
                    else:
                        break
            
            if ai.num > num:
                print('AI wins! You lose :(')
                print('You had {} for a total of {}.'.format(hand, num))
                print('AI had {} for a total of {}'.format(ai.hand, ai.num))
                if PlayAgain() == 1:
                    num = 0
                    hand = []
                    bjstate.start()
                    pass
                else:
                    break
            elif ai.num < num:
                print('You win!')
                print('You had {} for a total of {}.'.format(hand, num))
                print('AI had {} for a total of {}'.format(ai.hand, ai.num))
                if PlayAgain() == 1:
                    num = 0
                    hand = []
                    bjstate.start()
                    pass
                else:
                    break
            else:
                print('It\'s a tie!')
                if PlayAgain() == 1:
                    num = 0
                    hand = []
                    bjstate.start()
                    pass
                else:
                    break
                
        else:
            print('Wrong input recieved!')

    # check
    # end
    print('\n\nThank you for playing!')