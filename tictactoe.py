# write your code here
x_win = False
o_win = False
win = []


def game_state(board):
    global x_win
    global o_win
    global draw

    # check if rows are the same
    if rows[0][0] == rows[1][1] == rows[2][2]:  # First, the diagonals
        x_win = rows[0][0] == 'X'
        o_win = rows[0][0] == 'O'
    elif rows[0][2] == rows[1][1] == rows[2][0]:
        x_win = rows[2][0] == 'X'
        o_win = rows[2][0] == 'O'
    for i in range(3):
        if rows[i][0] == rows[i][1] == rows[i][2]:  # horizontal rows
            if rows[i][0] == 'X':
                x_win = True
            elif rows[i][0] == 'O':
                o_win = True
        if rows[0][i] == rows[1][i] == rows[2][i]:  # vertical rows
            if rows[0][i] == 'X':
                x_win = True
            elif rows[0][i] == 'O':
                o_win = True
    return [x_win, o_win]


first_row = [' ', ' ', ' ']
second_row = [' ', ' ', ' ']
third_row = [' ', ' ', ' ']
rows = [first_row, second_row, third_row]


print(f"""---------
| {rows[0][0]} {rows[0][1]} {rows[0][2]} |
| {rows[1][0]} {rows[1][1]} {rows[1][2]} |
| {rows[2][0]} {rows[2][1]} {rows[2][2]} |
---------""")
# get new coord, run checks
move_count = 0
while True:
    new_coord = input('Enter the coordinates: ').split()
    # Check that there's numbers
    # check that it's valid
    valid = {1, 2, 3}
    for i in range(len(new_coord)):
        try:
            new_coord[i] = int(new_coord[i])
        except TypeError:
            print("You should enter numbers!")
            continue
    if not new_coord[0] in valid:
        print('Coordinates should be from 1 to 3!')
        continue
    if not new_coord[1] in valid:
        print('Coordinates should be from 1 to 3!')
        continue
    coord1 = new_coord[0] - 1
    coord2 = new_coord[1] - 1
    if rows[coord1][coord2] != ' ':
        print('This cell is occupied! Choose another one!')
    else:
        if (move_count % 2) == 0:
            rows[coord1][coord2] = 'X'
        else:
            rows[coord1][coord2] = 'O'
    print(f"""
    ---------
    | {rows[0][0]} {rows[0][1]} {rows[0][2]} |
    | {rows[1][0]} {rows[1][1]} {rows[1][2]} |
    | {rows[2][0]} {rows[2][1]} {rows[2][2]} |
    ---------""")
    move_count += 1
    win = game_state(rows)
    if any(win) or move_count == 9:
        break
if o_win:
    print("O wins")
elif x_win:
    print("X wins")
else:
    print('Draw')
