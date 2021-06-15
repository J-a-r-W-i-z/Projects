import environment
state=environment.initial_state()
pl=1

def mm(state1):
    global pl
    list=[]
    ava_actions=environment.actions(state1)
    for p in ava_actions:
        nextstate=environment.result(state1,p)
        if environment.terminal(nextstate):
            value=environment.utility(nextstate)
            return (p,value*0.9)
        x=mm(nextstate)
        list.append((p,x[1]))
    if environment.player(state1)=='X':
        pl=1
    else:
        pl=-1
    if pl==-1:
        list.sort(key= lambda x: x[1])
    if pl==1:
        list.sort(key=lambda x: x[1],reverse=True)
    a=list[0]
    return((a[0],a[1]*0.9))


def humanplay():
    global state
    coo=int(input("Enter Coordinates from 00 to 22: "))
    y=coo//10
    x=coo%10
    action=(x,y)
    ava_actions=environment.actions(state)
    while(action not in ava_actions):
        print("Illegal coordinates")
        coo=int(input("Enter Coordinates from 00 to 22: "))
        x=coo//10
        y=coo%10
        action=(x,y)
    state=environment.result(state,action)
    environment.display(state)

def AIplay():
    global state,pl
    print("AI playing...")
    print()
    state1=state
    if state==environment.initial_state():
        action=[(1,1)]
    else:
        action=mm(state1)
    state=environment.result(state,action[0])
    environment.display(state)
        

def play():
    c=input("Do you want to play first? (y/n)")
    c=c.lower()
    if c=='y':
        pl=-1
        humanplay()
    while(True):
        AIplay()
        if environment.terminal(state):
            break
        print("Your Turn...")
        humanplay()
        if environment.terminal(state):
            break
    if environment.utility(state)==0:
        print("Game Tied!")
    else:
        print("AI has won the game!!")

play()
    