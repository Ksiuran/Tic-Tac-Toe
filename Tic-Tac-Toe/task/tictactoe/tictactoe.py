import string


# For some reason they wanted the grid co-ords to look like
# (1,3) (2,3) (3,3)
# (1,2) (2,2) (3,2)
# (1,1) (2,1) (3,1)
# Rather than the top left being 1,1 and the bottom right being 3,3
# check if there's a line of Xes
def xcheck(lst):
    if lst[0] == 'X' and lst[1] == 'X' and lst[2] == 'X':  # horizontal top
        # print("horizontal top x") these commented print statements were for debugging
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


# Check for a line of Os
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
    # Check if there are blank spaces and if neither x or o has a line
    if lst.count(' ') > 0 and not xcheck(lst) and not ocheck(lst):
        # if so, the game is still running
        return True
    else:
        return False


def play(lst):
    # This is the logic for editing the location of the chosen cell
    # converting between locations in the list and the co-ords they wanted me to use above
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
                        # What's going on with the x and o here is I always have one
                        # at the end of the array, to tell me what comes next without having
                        # to do any additional vars and args
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

# create a str with 9 spaces
cells = "         "
game = [x for x in cells]
# convert those spaces into an array
playing = 1
# put an X at the end so that X has first play
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
