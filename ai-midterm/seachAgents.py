from problems import Node
from problems import SingleFoodSearchProblem as SFSP
import fringes

'''
Approach
- Start with a frontier that contains the initial state
- Start with an empty explored set
- Repeat: 
    + If the frontier is empty -> no solution 
    + Remove a node from the frontier
    + If that node contains goal state -> return solution
    + Add the node to the explored set
    + expand node, add resulting nodes to the frontier if they are not already in the frontier or explored set

* Note: https://web.goodnotes.com/s/TYBbjwsEupC3Rir22zGTis#page-3
'''

def dfs(problem : SFSP):
    # print("Problem Info: ")
    # print("height: ", problem.height, "  - width: ", problem.width)
    # print("initial_state: ", problem.initial_state.state)
    # print("food_location: ", problem.food_location.state, " action: ", problem.food_location.action)
    
    frontier = fringes.Stack()
    explored_set = set()
    start = Node(problem.initial_state.state, None, None, 0)
    frontier.push(start)
    while frontier.is_empty() == False:
        n = frontier.pop()
        if problem.goal_test(n.state): # backtracking the steps from the goal to initial state
            n.action = "Stop"
            actions = []
            while n.parent is not None:
                actions.append(n.action)
                n = n.parent
            actions.reverse() # actions from initial state to goal state
            return actions
        
        explored_set.add(n.state)

        a = problem.successor(n) 
        for node in a:
            if(not frontier.contains(node)) and (node.state not in explored_set):  
                frontier.push(node)      
     
def bfs(problem : SFSP):
    # print("Problem Info: ")
    # print("height: ", problem.height, "  - width: ", problem.width)
    # print("initial_state: ", problem.initial_state.state)
    # print("food_location: ", problem.food_location.state, " action: ", problem.food_location.action)
    
    frontier = fringes.Queue()
    explored_set = set()
    start = Node(problem.initial_state.state, None, None, 0)
    frontier.enqueue(start)
    while frontier.is_empty() == False:
        n = frontier.dequeue()
        if problem.goal_test(n.state): # backtracking the steps from the goal to initial state
            n.action = "Stop"
            actions = []
            while n.parent is not None:
                actions.append(n.action)
                n = n.parent
            actions.reverse() # actions from initial state to goal state
            return actions
        
        explored_set.add(n.state)

        a = problem.successor(n) 
        for node in a:
            if(not frontier.contains(node)) and (node.state not in explored_set):  
                frontier.push(node)   
         
# problem_dfs = dfs(SFSP())
# print(problem_dfs)

problem = SFSP()
problem_bfs = bfs(SFSP())
problem_dfs = dfs(SFSP())

problem.animate(problem_bfs)