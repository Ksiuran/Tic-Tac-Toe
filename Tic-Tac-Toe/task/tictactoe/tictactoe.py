import string


def xcheck(lst):
    if lst[0] == 'X' and lst[1] == 'X' and lst[2] == 'X':  # horizontal top
        # print("horizontal top x")
        return True
    elif lst[0] == 'X' and lst[3] == 'X' and lst[6] == 'X':  # vertical left
        # print("vertical left x")
        return True
    elif lst[1] == 'X' and lst[4] == 'X' and lst[7] == 'X':  # vertical mid
        # print("vertical mid x")
        return True
    elif lst[2] == 'X' and lst[5] == 'X' and lst[8] == 'X':  # vertical right
        # print("vertical right x")
        return True
    elif lst[3] == 'X' and lst[4] == 'X' and lst[5] == 'X':  # horizontal mid
        # print("horizontal mid x")
        return True
    elif lst[6] == 'X' and lst[7] == 'X' and lst[8] == 'X':  # horizontal bottom
        # print("horizontal bottom x")
        return True
    elif lst[0] == 'X' and lst[4] == 'X' and lst[8] == 'X':  # Diagonal LT to BR
        # print("Diagonal LT to BR x")
        return True
    elif lst[2] == 'X' and lst[4] == 'X' and lst[6] == 'X':  # Diagonal RT to BL
        # print("Diagonal RT to BL x")
        return True
    else:
        return False


def ocheck(lst):
    if lst[0] == 'O' and lst[1] == 'O' and lst[2] == 'O':  # horizontal top
        # print("horizontal top o")
        return True
    elif lst[0] == 'O' and lst[3] == 'O' and lst[6] == 'O':  # vertical left
        # print("vertical left o")
        return True
    elif lst[1] == 'O' and lst[4] == 'O' and lst[7] == 'O':  # vertical mid
        # print("vertical mid o")
        return True
    elif lst[2] == 'O' and lst[5] == 'O' and lst[8] == 'O':  # vertical right
        # print("vertical right o")
        return True
    elif lst[3] == 'O' and lst[4] == 'O' and lst[5] == 'O':  # horizontal mid
        # print("horizontal mid o")
        return True
    elif lst[6] == 'O' and lst[7] == 'O' and lst[8] == 'O':  # horizontal bottom
        # print("horizontal bottom o")
        return True
    elif lst[0] == 'O' and lst[4] == 'O' and lst[8] == 'O':  # Diagonal LT to BR
        # print("Diagonal LT to BR o")
        return True
    elif lst[2] == 'O' and lst[4] == 'O' and lst[6] == 'O':  # Diagonal RT to BL
        # print("Diagonal RT to BL o")
        return True
    else:
        return False


def running(lst):
    if lst.count(' ') > 0 and not xcheck(lst) and not ocheck(lst):
        return True
    else:
        return False


def play(lst):
    going = 1
    while going == 1:
        x, y = input("Enter the coordinates:").split()
        if x in string.digits:
            x = int(x)
            y = int(y)
            if x in range(1, 4) and y in range(1, 4):
                if y == 3:
                    loc = x - 1
                elif y == 2:
                    loc = 3 + x - 1
                else:
                    loc = 6 + x - 1
                if lst[loc] == " ":
                    if lst[-1] == "X":
                        lst.pop(loc)
                        lst.insert(loc, "X")
                        lst.pop(-1)
                        lst.insert(len(lst), "O")
                    else:
                        lst.pop(loc)
                        lst.insert(loc, "O")
                        lst.pop(-1)
                        lst.insert(len(lst), "X")
                    return lst
                else:
                    print("This cell is occupied! Choose another one!")
            else:
                print("Coordinates should be from 1 to 3!")
        else:
            print("You should enter numbers!")


cells = "         "
game = [x for x in cells]
playing = 1
game.insert(len(game), "X")
while playing == 1:
    print("---------\n| {} {} {} |\n| {} {} {} |\n| {} {} {} |\n---------".format(game[0], game[1], game[2], game[3],
                                                                                  game[4], game[5], game[6], game[7],
                                                                                  game[8]))

    if running(game):
        game = play(game)
    elif xcheck(game):
        print("X wins")
        playing = 0
    elif ocheck(game):
        print("O wins")
        playing = 0
    else:
        print("Draw")
        playing = 0
