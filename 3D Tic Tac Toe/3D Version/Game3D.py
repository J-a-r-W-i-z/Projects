import sys
import random
import pickle
import gym_tictactoe.envs.tictactoe_env
from gym_tictactoe.envs.tictactoe_env import TicTacToeEnv, after_action_state, check_game_status, agent_by_mark

Q_value=open('Q-Values.txt','rb')
q_table=pickle.load(Q_value)
Q_value.close()

env=TicTacToeEnv()

class HumanAgent(object):
    def __init__(self, mark):
        self.mark = mark

    def act(self, ava_actions):
        while True:
            uloc = input("Enter location[000 - 222], q for quit: ")
            if uloc.lower() == 'q':
                return None
            try:
                action = uloc
                if action not in ava_actions:
                    raise ValueError()
            except ValueError:
                print("Illegal location: '{}'".format(uloc))
            else:
                break

        return self.mark + action

class AIAgent(object):
    def __init__(self, mark):
        self.mark = mark
        self.list=[]
        self.A={}
        self.max=-10
        self.max_state=env._world
    
    def act(self, ava_actions):

        self.list.clear()
        self.A.clear()
        self.max=-10
        for p in ava_actions:
            p=self.mark+p
            state=env._world
            next_state=after_action_state(state, p)
            self.list.append(str(next_state))
            self.A[str(next_state)]=p
        for j in self.list:
            if q_table.get(j,-11)>self.max:
                self.max=q_table.get(j)
                self.max_state=j
        if self.max==-10:
            action=random.choice(ava_actions)
            return self.mark + action
        action=self.A.get(str(self.max_state))
        return action
        
        
def play():
    agents = [AIAgent('1'),
              HumanAgent('2')]
    done=False
    while not done:
        agent=agent_by_mark(agents, str(env.show_turn()))
        if int(agent.mark)==2:
            print("Your Turn")
        else:
            print("Playing....")
        ava_actions = env.available_actions()
        action = agent.act(ava_actions)
        print(action)
        if action is None:
            sys.exit()

        state, reward, done, info = env.step(action)

        print()
        env.render()
        if done:
            env.show_result()
            print(env._world)
            break

if __name__ == '__main__':
    play()
