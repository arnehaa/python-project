#Game of rock paper scissors
import random

#List of allowed moves
moves = {1: 'rock', 2: 'paper', 3: 'scissors'}

#List of which moves beat other moves
move_rules = {'rock': 'scissors', 'paper':'rock', 'scissors': 'paper'}

#List of game results
results = {'Win': 0, 'Draw': 0, 'Loss': 0}

finish = False

while finish != True:
    #Generate a bot move, stored as an integer
    bot_move = moves[random.randint(1,len(moves))]
    
    #input(f"Pick your move: {moves}")
    player_move = moves[int(input(f"Pick your move: {moves}"))]
        
    result = ""
    #Decide who wins
    if bot_move == player_move:
        results['Draw'] += 1
        result = 'Draw'
    elif bot_move in move_rules[player_move]:
        results['Win'] += 1
        result = 'Win'
    else:
        results['Loss'] += 1
        result = 'Loss'

    print(f"You play {player_move} against {bot_move} > {result}")

    #Replay or end game
    finish = True if input(print(f"Replay? (y/n)")) == 'n' else False

print(f"Game ended.\nResults: {results}")