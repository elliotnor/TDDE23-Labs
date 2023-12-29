
#Task 3A
def new_board():
    """Creates a new board"""
    return {}


def is_free(board, x, y):
    """Checks if a selected coordinate is occupied or free"""
    if (x,y) in board: 
        return False #coordinates are already occupied
    else:
        return True 
    

def place_piece(board, x, y, player):
    """Place a piece at a selcted coordinate"""
    if is_free(board,x ,y):
        board[(x,y)] = player #places the peice at given coordinate
        return True
    else:
        return False #if coordinate is already occupied


def get_piece(board, x, y):
    """Show if a piece is at a selected coordinate"""
    if is_free(board, x, y) != True:   
        return board[(x,y)]
    else:
        return False


def remove_piece(board, x , y):
    """Removes a piece from the board"""
    if is_free(board, x, y) != True:
        board.pop((x, y))
        return True
    else:
        return False

def move_piece(board, old_x, old_y, new_x, new_y):
    """Moves the piece from one coordinate to another"""
    if is_free(board,old_x, old_y):
        return False
    
    elif not is_free(board, new_x, new_y):
        return False
    
    else:
        player_name = get_piece(board,old_x,old_y)
        remove_piece(board, old_x, old_y)
        place_piece(board, new_x, new_y, player_name)
        return True


def count(board, col_row,xy,plr):
    """Count the number of pieces on a selcted row"""
    num = 0 
    for pos, player in board.items():
        if col_row == "column" and xy == pos[0] and  plr == player:
            num += 1
        elif col_row == "row" and xy == pos[1] and  plr == player:
            num += 1
    return num

def nearest_piece (board, x, y):
    """Show the piece closest to a location"""
    from math import sqrt
    coord = list(board.keys())
    if board == {}:
        return False #Since there are no peices to compare
    x2, y2 = coord[0]
    for elements in coord:
        if sqrt((x - x2)**2 + (y-y2)**2 > sqrt((x - elements[0])**2 + (y - elements[1])**2)):
            x2 = elements[0]
            y2 = elements[1]
    return x2, y2


#-- Tests for A --#
"""
board = new_board()
place_piece(board, 500, 100, "spelare1")
print(move_piece(board,500, 100, 23,23))
print(is_free(board, 500, 100))
place_piece(board, 1, 100, "spelare2")
place_piece(board, 500, 100, "spelare2")
place_piece(board, 500, 200, "spelare2")
is_free(board, 500, 100)
get_piece(board, 500, 100)
get_piece(board, 666,666)
remove_piece(board, 500, 100)
remove_piece(board, 1, 1)
is_free(board, 500, 100)
"""

#Task 3B
def choose(n, k):
    """The main function, calculates n over k)"""
    simple_k = n - k
    if k > n or 0 > k or 0 > n:
        return "Invalid numbers!"
    if n < 2:
        return 1
    if k < simple_k:
        return fac1(n, simple_k) // fac2(k)
    if k > simple_k:
        return fac1(n, k) // fac2(simple_k)

def fac1( num1, num2):
    """Helper function #1"""
    if num1 <= num2:
        return 1
    else:
        return (num1 * fac1(num1-1, num2))

def fac2(num):
    """Helper function #2"""
    if 2 > num:
        return 1
    else:
        return num*fac2(num-1)

#-- Tests for B --#
assert choose(5, 3) == 10
assert choose(1000, 1) == 1000
assert choose(1000, 4) == 41417124750
assert choose(52, 5) == 2598960


