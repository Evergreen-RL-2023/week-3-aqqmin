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

class Agent():
    def __init__(self,r,c):
        self.row = r
        self.col = c
        self.gridcell = null
        self.rewards = 0
        self.actions = ['n','e','s','w']

    def step():
        act_index = rnd.randrange(0, 4)
        action = self.actions[act_index]
        self.rewards += get_reward(gridcell, action)

    def get_reward(gridcell):
        if ((gridcell.row == 0 and action == 'n') or (gridcell.col == 0 and action == 'w') or (gridcell.row == gridworld.size and action == 's') or (gridcell.col == gridworld.size and action == 'e')):
            reward = -1
        else:
            reward = gridcell.reward
        return reward

class GridWorld():
    def __init__(self, size):
        self.grid = []
        for i in range(size):
            print(i)
            self.grid.append([])
            for k in range(size):
                self.grid[i].append(GridCell(i,k))
                #print(f'creating: {i},{k}')

class GridCell():
    def __init__(self, r, c):
        # what else do you need?
        self.row = r
        self.col = c
        self.type = 0
        if self.type == 0:
            self.reward = 0
        if self.type == 1:
            self.reward = 10
        if self.type ==2:
            self.reward = 5
    
    def get_next_cell(self, action):
        r = self.row
        c = self.col
        print(f'row {r} , col {c}')
        # action is 'n', 'e', 's', 'w'
        '''
        match action:
           case 'n':
              r -= 1
           case _:
              print(action, 'invalid action')
        '''

        return r,c
    

    def step():
        act_index = rnd.randrange(0, 4)
        action = actions[act_index]
        rwd = get_reward(action)


if __name__ == '__main__':
    rnd.seed(42)
    
    GridWorld(N)
    
    
    '''grid = []
    gcell = GridCell(1,1)
    gcell.get_next_cell('n')
    for i in range(N):
        grid.append([])
        for j in range(N):
            grid[i].append(GridCell(i,j))
            print(grid[i][j], end=' ')'''
