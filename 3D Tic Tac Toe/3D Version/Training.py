
import sys
import random
from tabnanny import check
import numpy as np
from gym.core import Env
import pickle
from collections import deque
import gym_tictactoe.envs.tictactoe_env 

alpha = 0.1
gamma = 0.9
epsilon = 0.2

env=gym_tictactoe.envs.tictactoe_env.TicTacToeEnv()
q_table={str(env._world):0}
try:
    Q_value=open('Q-Values.txt','rb')
    q_table=pickle.load(Q_value)
    Q_value.close()
except:
    print("Training for first Time")
list=[]
A={}     
stack=deque()                            

print("Playing 20000 Games to collect Data...")
for i in range(20000):
    if i%100==0: print(i)
    player=1
    done=False
    state=env.reset()
    result=0
    while not done:
        ava_actions = env.available_actions()
        if random.uniform(0,1)<epsilon:
            action=random.choice(ava_actions)
            action=str(player)+action
            next_state= gym_tictactoe.envs.tictactoe_env.after_action_state(state,action)
            result=gym_tictactoe.envs.tictactoe_env.check_game_status(next_state)
            if result==1:
                q_table.setdefault(str(next_state),1)
            elif result==2:
                q_table.setdefault(str(next_state),-1)
            else:
                q_table.setdefault(str(next_state),0)
        else:
            list.clear()
            A.clear()
            max=-10
            min=10
            for p in ava_actions:
                p=str(player)+p
                next_state= gym_tictactoe.envs.tictactoe_env.after_action_state(state,p)

                result=gym_tictactoe.envs.tictactoe_env.check_game_status(next_state)

                list.append(str(next_state))
                A[str(next_state)]=p

                if result==1:
                    q_table.setdefault(str(next_state),1)
                elif result==2:
                    q_table.setdefault(str(next_state),-1)
                else:
                    q_table.setdefault(str(next_state),0)
            
            if player==1:
                for j in list:
                    if q_table.get(j)>max:
                        max=q_table.get(j)
                        new_state=j
            
            if player==2:
                for j in list:
                    if q_table.get(j)<min:
                        min=q_table.get(j)
                        new_state=j
            action=A.get(str(new_state))

        next_state= gym_tictactoe.envs.tictactoe_env.after_action_state(state,action)
        if player==1: 
            player=2
        else: 
            player=1

        stack.append(str(next_state))

        state, reward, done, info = env.step(action)

        if done:
            a=gym_tictactoe.envs.tictactoe_env.check_game_status(next_state)
            if a==-1:
                print("Error")
            q_table[str(next_state)]= 1 if a==1 else -1
        

    next_state=stack.pop()
    Reward=q_table.get(str(next_state))

    
    while(len(stack) > 0):
        state=stack.pop()
        Q_n1=q_table.get(str(state))
        Q_n2=q_table.get(str(next_state))
        Q_n1=Q_n1*(1-alpha)+alpha*(gamma*Q_n2)
        q_table[str(state)]= Q_n1
        next_state=state

print("Trianing completed!\nReady to play!!")


Qvalues=open('Q-Values.txt','wb')
pickle.dump(q_table,Qvalues)
Qvalues.close()

    


