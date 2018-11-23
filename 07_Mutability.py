# This is a list of lists
game = "I want to play a game"
print(id(game))

def game_board(player=0, row=0, column=0, just_display=False):
    game = "A game"
    print(id(game))
    print(game)

print(game)
game_board()
print(game)