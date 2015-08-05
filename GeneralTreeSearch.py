__author__ = 'frank'

def successor_fn(state):
    return STATE_SPACE[state]

PROBLEM = 'Go to J'
INITIAL_STATE = {'Go to J':'A'}
GOAL_TEST = {'Go to J':'J'}
SUCCESSOR_FN = {'Go to J':successor_fn}

STATE_SPACE = {'A':['B', 'C'], 'B':['D', 'E'], 'C':['F', 'G'], 'D':[], 'E':[], 'F':[], 'G':['H', 'I', 'J'], 'H':[], 'I':[], 'J':[]}

def INSERT(node, queue):
    queue[:0] = [node]
    return queue

def INSERT_ALL(list, queue):
    for node in list:
        INSERT(node, queue)
    return queue

def EMPTY(queue):
    return len(queue) == 0

def REMOVE_FIRST(queue):
    if len(queue) != 0:
        first = queue[0]
        queue[0:1]=[]
        return first
    return []

def SOLUTION(node):
    return node.path();

def EXPAND(node, problem):
    successors = []
    for result in SUCCESSOR_FN[problem](node.STATE):
        s = Node(node)
        s.STATE = result
        s.PARENT_NODE = node
        s.DEPTH = node.DEPTH + 1
        successors = INSERT(s,successors)
    return successors

def TREE_SEARCH(problem, fringe):
    fringe = INSERT(MAKE_NODE(INITIAL_STATE[problem]), fringe)
    while True:
        node = REMOVE_FIRST(fringe)
        if GOAL_TEST[problem] == node.STATE : return SOLUTION(node)
        fringe = INSERT_ALL(EXPAND(node, problem), fringe)

def MAKE_NODE(state):
    return Node(state)

def run():
    print('Solution path')
    for node in TREE_SEARCH(PROBLEM, []):
        node.display()

run()

class Node:
    def __init__(self, state, parent = None, depth = 0, action = None):
        self.STATE = state
        self.PARENT_NODE = parent
        self.DEPTH = depth
    def path(self):
        x, result = self, [self]
        while x.PARENT_NODE:
            result.append(x.PARENT_NODE)
            x = x.PARENT_NODE
        return result
    def display(self):
        print(self, ' ', self.DEPTH)