# DW-blackjack
A simple python blackjack game! Comes with built in dealer AI.

### How to play
Simple blackjack rules: if you get 21 you win automatically, if you go over you lose. The aim is to get a higher value than your opponent or to blackjack.
Every turn you have two options:
- *Hit*: Add a card to your hand.
- *Stand*: Do not add a card to your hand. If you do this you cannot hit in subsequent turns.

### About the code
Dependencies: ``libdw``
Standard Python libraries used: ``random``, ``time``


#### ``class bjsm``
**B**lack**j**ack **S**tate **M**achine
Defines the start state for the state machine for the user and the AI. Function ``get_next_values`` is to find the subsequent states for given total value of hand.
- If hand value is 21, state is ``blackjack``
- If hand value is under 21, state is ``ok``
- If hand value is over 21, state is ``bust``


#### ``PlayAgain()``
Function to know whether player wants to play again or not.
Returns ``1`` if user wants to play again, ``0`` if they do not want to. ``ERROR`` is returned if there is an issue running the function. 


#### ``class AI``
Class that defines behavior of AI and it's functions

- ##### ``__init__()``
    Initialises the variables required for this class. It also initialises the state machine for the AI.
- ##### ``hit()``
    Simulates drawing of card from deck.
- ##### ``decide()``
    Decides if the AI should hit or stand. Probability of going over is calculated and a dice is rolled. If dice roll is lower than probability of going over then AI will hit, otherwise it will stand.
- ##### ``getnext()``
    Calculates the next state of the AI.

#### ``__main__``
Initialises player hand and state machine. Infinite loop that breaks out when user does not want to continue playing the game.
Random seed is generated every loop to ensure that the draws are truly random everytime.

**If player hits**
Player draws card, followed by AI. Game checks if player or AI gets busted or gets a blackjack. 

**If player stands**
AI hits every until it stands. Game checks if AI gets busted or gets a blackjack. If the checks pass then the script checks for which player has won by comparing the value of hands of the player and the AI.