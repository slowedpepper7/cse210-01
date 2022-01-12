#Tic Tac Toe Game, Using functions, while loops, and if statments
# Author - Ethan Shaw
def create_board(spaces):
    print(f'{spaces[0]}|{spaces[1]}|{spaces[2]}')
    print(f'-+-+-')
    print(f'{spaces[3]}|{spaces[4]}|{spaces[5]}')
    print(f'-+-+-')
    print(f'{spaces[6]}|{spaces[7]}|{spaces[8]}')

def get_input_X(spaces):
    selected_space = int(input('Which space would you like to add an x to?'))
    while 5 != 0:
        if selected_space in spaces:
            return selected_space
        else:
            print('Please enter a valid space')
            selected_space = int(input('Which space would you like to add an x to?'))
    
def add_X(s, spaces):
    s = s - 1
    spaces[s] = 'x'
def get_input_O(spaces):
    selected_space = int(input('Which space would you like to add an o to?'))
    while 5 != 0:
        if selected_space in spaces:
            return selected_space
        else:
            print('Please enter a valid space')
            selected_space = int(input('Which space would you like to add an x to?'))
def add_O(s, spaces):
    s = s - 1
    spaces[s] = 'o'

def create_list():
    return [1, 2, 3, 4, 5, 6, 7, 8, 9]

def check_x_win(spaces):
    row_1 = spaces[0:3]
    row_2 = spaces[3:6]
    row_3 = spaces[6:9]
    if row_2[1] == 'x':
        if row_1[0] == 'x':
            if row_3[2] =='x':
                return True
        elif row_1[2] == 'x':
            if row_3[0] == 'x':
                return True
    if row_2 and row_3 and row_1 == ['x', 'x', 'x']:
        return True
    if row_1[0] == 'x' and row_2[0] == 'x' and row_3[0] == 'x':
        return True
    if row_1[1] == 'x' and row_2[1] == 'x' and row_3[1] == 'x':
        return True
    if row_1[2] == 'x' and row_2[2] == 'x' and row_3[2] == 'x':
        return True
    return False

def check_o_win(spaces):
    row_1 = spaces[0:3]
    row_2 = spaces[3:6]
    row_3 = spaces[6:9]

    if row_2[1] == 'o':
        if row_1[0] == 'o':
            if row_3[2] =='o':
                return True
        elif row_1[2] == 'o':
            if row_3[0] == 'o':
                return True
    if row_2 and row_3 and row_1 == ['o', 'o', 'o']:
        return True
    if row_1[0] == 'o' and row_2[0] == 'o' and row_3[0] == 'o':
        return True
    if row_1[1] == 'o' and row_2[1] == 'o' and row_3[1] == 'o':
        return True
    if row_1[2] == 'o' and row_2[2] == 'o' and row_3[2] == 'o':
        return True
    
def main():
    turn = 1
    spaces = create_list()
    win = False
    while win == False:
        if check_x_win(spaces) != True:
            if check_o_win(spaces) != True:
                if turn % 2 == 0:
                    create_board(spaces)
                    selected_space = get_input_O(spaces)
                    add_O(selected_space, spaces)
                    turn += 1
                else:
                    create_board(spaces)
                    selected_space = get_input_X(spaces)
                    add_X(selected_space, spaces)
                    turn += 1
            else:
                win = True
                print('Congratulations o won the game!')
        else: 
            win = True
            print('Congratulations x won the game!')
        if turn == 10:
            print('The game is a tie!')
            win = True
main()