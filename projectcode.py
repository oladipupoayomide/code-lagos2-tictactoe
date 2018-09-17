score=0

choices=[]

for x in range(0, 9):
    choices.append(str(x + 1))
 
playerOneTurn = True
winner = False

def printBoard():
    print( '\n _____')
    print( '|' + choices [0] + '|' + choices[1] + '|' + choices[2] + '|')
    print( '_____')
    print( '|' + choices[3] + '|' + choices[4] + '|' + choices[5] + '|')
    print( '_____')
    print( '|' + choices[6] + '|' + choices[7] + '|' + choices[8] + '|')
    print( '_\n')

while not winner:
    printBoard()

    if playerOneTurn:
        print("player 1:")
    else:
        print("player 2:")

    try:
        choice = int(input(">> "))
    except:
        print("please enter valid field")
        continue
    
    if choices[choice -1] == 'x' or choices[choice-1] == '0':
       print("illegal move, please try again")
       continue
               
    if playerOneTurn:
        choices[choice - 1] = 'x'
    else:
        choices[choice - 1] = '0'
               
    playerOneTurn = not playerOneTurn

    for x in range(0, 3):
        y = x * 3
        if (choices[y] == choices[(y + 1)] and choices[y] == choices[(y+2)]):
            winner=True
            printBoard()

        if((choices[0] == choices[4] and choices[0] == choices[8]) or
           (choices[2] == choices[4] and choices[4] == choices[6])):
            winner = True
            printBoard()

            score = str(score+1)

print("Player " + str(int(playerOneTurn + 1)) + "wins!\n" + "with\n" + score + "point(s)")

print("Next round we can do this!")
        
    
