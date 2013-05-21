import sys

f_input = open(sys.argv[1])
#problems = int(f_input.readline().rstrip())

def checkwin(board):
    def checkline(score):
        if score>3:
            return "X won"
        elif score<0:
            return None
        elif score<1:
            return "O won"
        else:
            return None
        
    for i in xrange(4):
        if not checkline(sum(board[i])) is None:
            return checkline(sum(board[i]))
    for i in xrange(4):
        if not checkline(sum([row[i] for row in board])) is None:
            return checkline(sum([row[i] for row in board]))
    if not checkline(sum([board[i][i] for i in xrange(4)])) is None:
            return checkline(sum([board[i][i] for i in xrange(4)]))
    if not checkline(sum([board[i][-(i+1)] for i in xrange(4)])) is None:
            return checkline(sum([board[i][-(i+1)] for i in xrange(4)]))

    ## draw or not complete ##
    if sum([sum(line) for line in board])>0:
        return "Draw"
    else:
        return "Game has not completed"
        
        
def transrate(character):
    if character == "X":
        return 1
    elif character == "O":
        return 0
    elif character == "T":
        return 0.5
    elif character == ".":
        return -20
    

linenums = int(f_input.readline().rstrip())
for i in xrange(linenums):
    board = []
    for j in xrange(4):
        board.append([transrate(c) for c in f_input.readline().rstrip()])
    f_input.readline()
    sys.stdout.write("Case #"+str(i+1)+": "+checkwin(board)+"\n")


