game_map = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]


# Add X or O in the list
def addElement(game, player, position):
    try:
        # Check if an already exists
        if game[position[0]][position[1]] == 0:
            game[position[0]][position[1]] = player
        else:
            print("An Entry already exists")
        return game
    except IndexError as e:
        print("We have error ", e)
    except Exception as p:
        print("We have error ", p)


# Winner by horizontal line
def horizontalVictory(game):
    for row in game:
        counter = 0
        foo = row[0]
        length = len(row)
        for element in row:
            if element == foo and foo != 0:
                counter += 1
                if counter == length:
                    return True

    return False


def verticalVictory(game):
    for col in range(len(game)):
        check = []
        for row in game:
            check.append(row[col])
        if check.count(check[col]) == len(check) and check[col] != 0:
            print("Winner!")


def diagonalVictory(game):
    check = []
    for row in range(len(game)):
        check.append(game[row][row])
    if check.count(check[row]) == len(check) and check[row] != 0:
        print("Winner!")

diagonalVictory(game_map)
