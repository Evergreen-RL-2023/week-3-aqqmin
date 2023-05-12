import random as rnd

S = 5 #Size of gridworld
E = 1 #Epsilon
G = .9 #gamma, discount rate


class GridWorld():

    def __init__(self, size, agentR, agentC):
        self.grid = [] #store the grid in a list
        self.size = size #set the size of the world
        for i in range(size): #create rows
            self.grid.append([]) #put an empty list in each row
            for k in range(size): #create columns
                self.grid[i].append(GridCell(i,k,self)) #put a cell in each row,col
        self.agent = Agent(agentR,agentC,self) #create agent

class GridCell():

    def __init__(self, r, c, gridworld):
        self.gridworld = gridworld
        self.row = r
        self.col = c
        
        self.action_vals = {'n':0,'e':0,'s':0,'w':0}
        self.reward = 0
        self.type = 0
        self.visits = 0
        self.value = 0

        if self.row == 0 and self.col == 1:
            self.type = 1
        if self.row == 0 and self.col == 3:
            self.type = 2

        if self.type == 1:
            self.reward = 10
            
        elif self.type == 2:
            self.reward = 5

    def get_outcome(self, action):
        reward = 0
        #handle boarder movement and reward
        if ((self.row == 0 and action == 'n') or (self.col == 0 and action == 'w') or (self.row == (self.gridworld.size - 1) and action == 's') or (self.col == (self.gridworld.size - 1) and action == 'e')):
            reward = -1
            next_cell = self
            #print("ouch")

        else:
            #handle special movement cases
            if self.type == 1: 
                next_cell = self.gridworld.grid[4][1]

            elif self.type == 2:
                next_cell = self.gridworld.grid[2][3]
            #otherwise move one space
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
            #reward is from cell we are moving out of
            reward = self.reward

        #outcome is a tuple, (reward, next_cell)
        return reward, next_cell  

class Agent():

    def __init__(self,r,c,gridworld):
        self.gridworld = gridworld
        self.gridcell = gridworld.grid[r][c]
        self.actions = ['n','e','s','w']

    def step(self):
        action = rnd.choice(self.actions)
        
        '''
        choice_vals = {}
        for choice in self.actions:
            choice_vals[choice] = self.gridcell.get_outcome(choice)[1].value
        running_val = min(list(choice_vals.values()))
        choice_key = 's'
        for key in list(choice_vals.keys()):
            running_key = key
            if choice_vals[running_key] > running_val:
                 choice_key = running_key

        if (rnd.random() > E):
            action = choice_key
        '''

        self.traverse(action)

    def traverse(self,action):
        #get the new cell that will be moved to, and the reward, in a tuple
        outcome = self.gridcell.get_outcome(action)
        #compute the value for the cell based on the reward for leaving it, and the average of the values of ceslls you will enter for all possible actions
        self.gridcell.value =  outcome[0] + G* (.25 * outcome[1].get_outcome('n')[1].value + .25 * outcome[1].get_outcome('e')[1].value + .25 * outcome[1].get_outcome('s')[1].value + .25 * outcome[1].get_outcome('w')[1].value)
        #move to the new cell
        self.gridcell = outcome[1] 
        self.gridcell.visits+=1
        #print(action)

    def sweep(self):
        for row in self.gridworld.grid:
            for gridcell in row:
                rewards = []
                for action in self.actions:
                    next = gridcell.get_outcome(action)
                    rewards.append(next[0]+G*next[1].value)
                gridcell.value =  max(rewards)    
                

class Test():
    def __init__(self):
        print("made a test!!")

def main():

    rnd.seed(42)
    gridworld = GridWorld(S,2,2)
    
    print(gridworld.grid[4][0])
    print(gridworld.grid[4][0].get_outcome('s'))
    print(gridworld.grid[0][4].get_outcome('e'))

    for i in range(10000):
        gridworld.agent.sweep()

    for i in range(S):
        for j in range(S):
            print(f"cell {i} , {j} has value {gridworld.grid[i][j].value} and {gridworld.grid[i][j].visits} visits")


if __name__ == '__main__':
    main()