"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    a=(board[0].count(X)+board[1].count(X)+board[2].count(X))
    b=(board[0].count(O)+board[1].count(O)+board[2].count(O))
    if a-b==0:
        return X
    else:
        return O

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    c=set()
    for i in range(3):
        for j in range(3):
            if board[i][j]==None:
                c.add((i,j))
    return c


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    d=copy.deepcopy(board)
    if not d[action[0]][action[1]]==None:
        raise Exception
    e=player(board)
    d[action[0]][action[1]]=e
    return d
    

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if check(X,board)==True:
        return X
    elif check(O,board)==True:
        return O
    else:
        return None

def check(e,board):
    """
    Returns True if e won the game, False otherwise
    """
    for i in range(3):
        if board[i]==[e,e,e]:
            return True
    for i in range(3):
        if board[0][i]==e and board[1][i]==e and board[2][i]==e:
            return True
    if board[0][0]==e and board[1][1]==e and board[2][2]==e:
        return True
    elif board[0][2]==e and board[1][1]==e and board[2][0]==e:
        return True
    else:
        return False
    

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    f=winner(board)
    if not f==None:
        return True
    g=actions(board)
    if len(g)==0:
        return True
    else:
        return False
    


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    f=winner(board)
    if f==X:
        return 1
    elif f==O:
        return -1
    else:
        return 0
  
def display(board):
    """
    Prints the board to the terminal
    """
    for i in board:
        for j in i:
            if j==None:
                print('__',end="\t")
                continue
            print(j,end="\t")
        print()
        print()
    return None


def recursive(w,k):
    g=actions(w)
    b=set()   
                                           
    for i in g: 
                                      
        a=result(w,i)
        if not terminal(a): 
            k=not k
            b.add(recursive(a,k))
            k=not k
        else:   
            return utility(a)         
    if k==False:
        return max(b)
    elif k==True:
        return min(b)


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if player(board)==X:
        k=True
        l=True
    elif player(board)==O:
        k=False
        l=False
    if board[1][1]==None:
        return(1,1)
    m={}
    
    action=actions(board)
    w=copy.deepcopy(board)
    for i in action:
        n=result(board,i)
        if terminal(n):
            return i
        p={i:recursive(n,k)}
        m.update(p)
    if l==True:
        v=list(m.values())
        k=list(m.keys())
        s=(k[v.index(max(v))])
        return s
    elif l==False:
        v=list(m.values())
        k=list(m.keys())
        s=(k[v.index(min(v))])
        return s