# This is a list of lists
game = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]


def game_board():
    print("   1  2  3")
    for count, row in enumerate(game):
        print(count, row)


game_board()

game[0][1]=1

game_board()
