import sys
import os

class Node:
    def __init__(self, state, parent, action, path_cost):
         self.state = state
         self.parent = parent
         self.action = action
         self.path_cost = path_cost

class SingleFoodSearchProblem:

    def __init__(self):
        with open(sys.argv[1]) as file:
            maze = file.read()
        
        # 'maze' list with each element is a line in text file
        maze = maze.splitlines()
        
        # maze's height and width
        self.height = len(maze)
        self.width = len(maze[0])
        
        bank_cells = []
        walls = []
        for r in range(self.height):
            row = []
            for c in range(self.width):
                if maze[r][c] == "P":
                    # self.initial_state =  (r, c)
                    self.initial_state = Node((r, c), None, None, 0)
                    row.append(False)
                elif maze[r][c] == ".":
                    # self.food_location = (r, c)
                    self.food_location = Node((r, c), None, "Stop", 0)
                    row.append(False)
                elif maze[r][c] == " ":
                    row.append(False)
                    bank_cells.append(Node((r, c), -1, -1, 0))
                else:
                    row.append((r, c))
            walls.append(row)
        self.walls = walls
        self.bank_cells = bank_cells
    
    def print_maze(self):
        print()
        for i, row in enumerate(self.walls):
            for j, col in enumerate(row):
                if col:
                    print("%", end="")
                elif (i, j) == self.initial_state.state:
                    print("P", end="")
                elif (i, j) == self.food_location.state:
                    print(".", end="")
                else:
                    print(" ", end="")
            print()  
        print() 
    
    def goal_test(self, state):
        return state == self.food_location.state
    
    def path_cost(self, node: Node):
        return node.path_cost
    
    def successor(self, node: Node):
        successors = []
        r, c = node.state
        actions = [
            ("N" , (r - 1, c)), # up
            ("S" , (r + 1, c)), # down
            ("W" , (r, c - 1)), # left
            ("E" , (r, c + 1)), # right
            ("Stop" , (r, c)) 
        ]
        
        for a in actions:
            r = a[1][0]
            c = a[1][1]
            if 0 <= r < self.height and 0 <= c < self.width and a[1] != self.walls[r][c]: # not out of range and not a wall
                successors.append(
                    Node(
                        state = (r, c),
                        action = a[0],
                        parent = node,
                        path_cost = node.path_cost + 1
                    )
                )
        # for i in range(len(successors)):
        #     print(successors[i].state, " ", successors[i].action)
        
        return successors
        
    def animate(self, actions):
        print(actions)
        print("\n", len(actions))
        input() # hit enter to clear the screen
        os.system('cls')
        
        i = 0
        initial_location = self.initial_state.state
        p_locations = []
        p_actions = []
        p_locations.append(initial_location)
        r, c = initial_location
        dict = [
            ("N" , (r - 1, c)), # up
            ("S" , (r + 1, c)), # down
            ("W" , (r , c - 1)), # left
            ("E" , (r, c+ 1)), # right
            ("Stop" , (r, c)) 
        ]
        for a in actions:
            for i in dict:
                if a == i[0] and len(p_locations) > 0:
                    tmp = p_locations.pop()
                    print(tmp)
                    if tmp == "N":
                        r = tmp[0] - 1
                        c = tmp[1] 
                        p_locations.append((r, c))
                    if tmp == "S":
                        r = tmp[0] + 1
                        c = tmp[1]
                        p_locations.append((r,c))
                    if tmp == "W":
                        r = tmp[0]
                        c = tmp[1] - 1
                        p_locations.append((r,c))
                    if tmp == "E":
                        r = tmp[0]
                        c = tmp[1] + 1
                        p_locations.append((r,c))
                    if tmp == "Stop":
                        r = tmp[0]
                        c = tmp[1]
                        p_locations.append((r,c))
                          
        
        print(p_locations)
        print(p_actions)
        
        
m = SingleFoodSearchProblem()
# print(m.height)
# print(m.bank_cells[0].state)
# print(m.initial_state.state)
# m.print_maze() 
# print(m.walls)

# t = m.successor(Node((3,11), None, None, 0))
# for i in range(len(t)):
#     print(t[i].state, " [" , t[i].action,  "] ", t[i].path_cost)

                 
        
        
        