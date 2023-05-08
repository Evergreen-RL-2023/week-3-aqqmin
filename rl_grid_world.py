### NICOLAS QUINN ALLEN

'''
template: Richard Weiss, April 2023
grid world simulation 
you can do this in O-O, functional, or imperative style
I used O-O here

for O-O, there would be a GridCell class, which is also the state of the agent.
What are the instance methods?
you want to choose an action, get a reward and determine the next state
in the first version, the policy is random, ie the action is chosen randomly from the 4
steps:
initialize the grid
initialize the position of the agent
loop a number of steps
choose an action and compute the result


useful Python: match case, randrange, 
match repuires Python 3.10
'''
import numpy as np
import random as rnd

N = 5   #grid size
D = .95 #discount

class Agent():
    def __init__(self,r,c,gridworld):
        self.gridworld = gridworld
        self.gridcell = gridworld.grid[r][c]
        self.rewards = 1
        self.actions = ['n','e','s','w']
        self.steps_since_reward = []

    def status(self):
        print(f'I am at {self.gridcell.row}, {self.gridcell.col}')

    def step(self):
        act_index = rnd.randrange(0, 4)
        action = self.actions[act_index]
        best_value = max(self.gridcell.vals, key=self.gridcell.vals.get)
        #lets explore about .25 of the time!
        if (rnd.random()>self.gridworld.E):
            action = best_value
        self.rewards += self.traverse(action)


    def traverse(self, action):
        print(f"traversing {action} !")
        self.steps_since_reward.append((self.gridcell,action))
        outcome = self.gridcell.get_outcome(action)        
        if outcome[0] != 0:
            for i in range((len(self.steps_since_reward)-1),-1,-1):
                step = self.steps_since_reward[i]
                action_taken = step[1]
                step_discount = (D**(len(self.steps_since_reward)-i-1))

                new_val = (step[0].vals[action_taken] + outcome[0] * step_discount)/2
                step[0].vals[action_taken] = new_val
                
                new_val_opt = (step[0].vals_opt[action_taken] + outcome[0] * step_discount)/2
                step[0].vals_opt[action_taken] = new_val_opt
                step[0].visits+=1
                   
            self.steps_since_reward = []

        #self.gridcell.vals[action] = (self.gridcell.vals[action] + outcome[0])/2
        self.gridcell = outcome[1]
        return outcome[0]
        

class GridWorld():
    def __init__(self, size, agentR, agentC):
        self.E = .25
        self.grid = []
        self.size = size
        for i in range(size):
            print(i)
            self.grid.append([])
            for k in range(size):
                self.grid[i].append(GridCell(i,k,self))
        self.agent = Agent(agentR,agentC,self)
        self.agent.status()


class GridCell():
    def __init__(self, r, c, gridworld):
        # what else do you need?
        self.gridworld = gridworld
        self.row = r
        self.col = c
        self.vals = {'n':1,'e':1,'s':1,'w':1}
        self.vals_opt = {'n':1,'e':1,'s':1,'w':1}
        self.reward = 0
        self.type = 0
        self.visits = 0

        if self.row == 0 and self.col == 1:
            self.type = 1
            print("Cell A now exists")
        if self.row == 0 and self.col == 3:
            self.type = 2
            print("Cell B now exists")

        if self.type == 1:
            self.reward = 10
        elif self.type == 2:
            self.reward = 5

    def get_outcome(self, action):
        if ((self.row == 0 and action == 'n') or (self.col == 0 and action == 'w') or (self.row == (self.gridworld.size - 1) and action == 's') or (self.col == (self.gridworld.size - 1) and action == 'e')):
            outcome = -1
            next_cell = self

        else:
            if self.type == 1: 
                next_cell = self.gridworld.grid[4][1]
            if self.type == 2:
                next_cell = self.gridworld.grid[2][3]
            else:
                match action:
                    case 'n':
                        next_cell = self.gridworld.grid[self.row-1][self.col]
                    case 'e':
                        next_cell = self.gridworld.grid[self.row][self.col+1]
                    case 's':
                        next_cell = self.gridworld.grid[self.row+1][self.col]
                    case 'w':
                        next_cell = self.gridworld.grid[self.row][self.col-1]
            outcome = next_cell.reward
            #get reward uppn entering cell, this will allow to map action values for each action from each cell
        return outcome, next_cell    

''' 
    def step():
        act_index = rnd.randrange(0, 4)
        action = actions[act_index]
        rwd = get_reward(action)
'''

if __name__ == '__main__':
    rnd.seed(42)
    world = GridWorld(N,N//2,N//2)
    s = 0
    while(s<1000):
        world.agent.step()
        s+=1

    for i in range (world.size):
        print(f"\n printing row {i}'s visits and values: ")
        for j in range (world.size):
            print(f"cell {i},{j} visited {world.grid[i][j].visits} times \n agent knows :{world.grid[i][j].vals}")

    
    for i in range (world.size):
        print(f"\n printing row {i}'s optimal ")
        for j in range (world.size):
            if world.grid[i][j].type != 0:
                print(f"cell {i},{j} is a warp cell")
            else:
                print(f"cell {i},{j} \n  optimal :{max(world.grid[i][j].vals, key=world.grid[i][j].vals.get)}")

