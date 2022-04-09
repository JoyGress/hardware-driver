from random import randint
from time import sleep
board = [[0,0,0],[0,0,0],[0,0,0]]
state = False # game state
pos = 1 # position
last = [0,0,0]

i = 0
forceEndTime = 0 # if this go to 3 minutes end game

def set_board(): # set led on PCB board
    for i in range(9):
        row = i // 3
        column = i % 3
        set_led(i,board[row][column])
        sleep(0.01) # delay between show led

def beginBoard(): # Randomize Board
    for i in range(9):
        # board[i // 3][i % 3] = 0 # all zero board
        board[i//3][i%3] = randint(0,1) # random board
    global state
    state = True
    if(check_solve2()):
        beginBoard()

def outBoard(): # Show board [ only for debugging ]
    global pos
    print("Current position : ", pos)
    for i in range(3):
        print(board[i])
    print("______________")

def check_solve(): # Check if the board is solved or not, if solved end the game
    solve = True
    for i in range(9):
        if(board[i//3][i%3] == 0):
            solve = False
    if(solve):
        global state
        state = False
        # outBoard()
        # print("done")

def check_solve2(): # Check if the board is solve (ONLY USE FOR PREVENTING GERERATING BOARD THAT ALREADY WON)
    solve = True
    for i in range(9):
        if(board[i//3][i%3] == 0):
            solve = False
    return solve

def push(a): # for pushing the buttom (switch the light at position a)
    a -= 1
    row = a // 3
    column = a % 3
    if row > 0:
        board[row-1][column] = 1 - board[row-1][column]
    if row < 2:
        board[row+1][column] = 1 - board[row+1][column]
    if column > 0:
        board[row][column-1] = 1 - board[row][column-1]
    if column < 2:
        board[row][column+1] = 1 - board[row][column+1]
    board[row][column] = 1 - board[row][column]
    set_board()
    check_solve()
    global pos
    pos = 1
    set_position_index(pos)

def moveleft(): # Move left
    global pos
    pos -= 1
    if(pos < 1):
        pos += 9
    set_position_index(pos)

def moveright(): # Move left
    global pos
    pos += 1
    if(pos > 9):
        pos -= 9
    set_position_index(pos)

def action(data): # Getting input for button from PCB then do action according to the input
    global last
    if(last[0] == 0 and data[0] == 1):
        last[0] = 1
        moveleft()
        # print("Current position : ", pos)
    elif(last[0] == 1 and data[0] == 0):
        last[0] = 0
    elif (last[1] == 0 and data[1] == 1):
        last[1] = 1
        moveright()
        # print("Current position : ", pos)
    elif (last[1] == 1 and data[1] == 0):
        last[1] = 0
    elif(last[2] == 0 and data[2] == 1):
        last[2] = 1
        push(pos)
        # print("Current position : ", pos)
    elif(last[2] == 1 and data[2] == 0):
        last[2] = 0

# main stats here

set_alarm(1)
set_position_index(1)
beginBoard()
print("Current position : 1")
while(state): # While game haven't ended, get input
    forceEndTime +=1 # increment time by 0.1 second (forceEndtime = 1800 is equal to 3 minute)
    if(forceEndTime == 1800): # if timer exceed 3 minute, ends game
        state = False
    outBoard()
    data = get_switch()
    action(data)
    sleep(0.1)
set_alarm(0)

# เนื่องจากมี delay ตอนปรับ LED ทำให้เวลาจริงอาจเกิน 3 นาที แต่นิดหน่อยช่างมัน
