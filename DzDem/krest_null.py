# init map
map=[1,2,3,
     4,5,6,
     7,8,9
     ]

# init victories
victories = [[0,1,2],
             [3,4,5],
             [6,7,8],
             [0,3,6],
             [1,4,7],
             [2,5,8],
             [0,2,8],
             [2,4,6],
             ]

# output map in screen
def print_maps():
    print(map[0],end=" ")
    print(map[1], end=" ")
    print(map[2])

    print(map[3], end=" ")
    print(map[4], end=" ")
    print(map[5])

    print(map[6], end=" ")
    print(map[7], end=" ")
    print(map[8])

# print krest and null
def step_map(step,symbol):
    ind=map.index(step)
    map[ind]=symbol

# get result game

def get_result():
    win=""
    for i in victories:
        if map[i[0]] == "X" and map[i[1]] == "X" and map[i[2]] == "X":
            win="X"
        if map[i[0]] == "O" and map[i[1]] == "O" and map[i[2]] == "O":
            win="O"
    return win

# main code
game_over=False
player1=True

while game_over==False:
    #1.print cart
    print_maps()
    #2.ques player
    if player1==True:
        symbol="X"
        step=int(input("Player_1, your step: "))
    else:
        symbol="O"
        step=int(input("Player_2, your step:"))
    step_map(step,symbol)
    win=get_result()
    if win!="":
        game_over=True
    else:
        game_over=False
    player1=not(player1)

# end game,print cart and result winner
print_maps()
print(f"Winner --> {win}")