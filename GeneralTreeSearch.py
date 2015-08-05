__author__ = 'frank'

INITIAL_STATE = {'A'}
GOAL_STATE = {'J'}

STATE_SPACE = {'A':['B', 'C'], 'B':['D', 'E'], 'C':['F', 'G'], 'D':[], 'E':[], 'F':[], 'G':['H', 'I', 'J'], 'H':[], 'I':[], 'J':[]}

class Node:
    def __init__(self, state, parent = None, depth = 0, action = None):
        self.STATE = state
        self.PARENT = parent
        self.DEPTH = depth
    def path(self):
        x, result = self, [self]
        while x.PARENT_NODE:
            result.append(x.PARENT_NODE)
            x = x.PARENT_NODE
        return result
    def display(self):
        print(self.STATE, ' ', self.DEPTH)
        asd
        fa
        sdf
        asdf
        asd
        fa
        sdf
        asdf
        abs(sdf
            asdf
        abs(sdf
            asdf
        abs(sdf
            asd
        fa
        sdf
        asd
        fa
        sdf
        ascii(df
              asdf
        abs(sdf
            ascii(df
                  asd
        fa
        sdf
        asd
        filterasd
        fa
        sdf))))))