import copy
import math
from enum import Enum
from collections import defaultdict

class Node:
    def __init__(self,parent, state = None, incoming_action=None):

        if not state:
            assert parent 
            assert incoming_action
            self._state = parent._state.next_state_from_action(incoming_action)
        else:
            self._state = state

        self._children = []
        self._actions = self._state.get_possible_actions()
        self._inmut_actions = copy.deepcopy(self._actions)
        self._visit_count = 0
        self._total_reward = defaultdict(int) 
        self._parent = parent
        self._incoming_action = incoming_action
        
    def actions(self):
        return self._inmut_actions

    def get_incoming_action(self):
        return self._incoming_action

    def get_parent(self):
        return self._parent
    
    def get_total_reward(self):
        assert(self._parent)
        last_player_to_move = self._parent._state._player
        wins = self._total_reward[last_player_to_move]
        loses = self._total_reward[-1*last_player_to_move]
        return wins - loses

    def get_visit_count(self):
        return self._visit_count

    def pop_action(self):
        assert len(self._actions) > 0
        return self._actions.pop()

    def append_child(self, node):
        self._children.append(node)

    def calculate_reward(self):
        return self._state.calculate_reward()

    def is_terminal(self):
        return self._state.is_terminal() 

    def register_visit(self,reward):
        self._visit_count += 1
        self._total_reward[reward] += 1

    def is_fully_expanded(self):
        return len(self._actions) == 0
    
    def get_children(self):
        return self._children
    
    def uct_val(self, exploration_factor = 1/pow(2,1/2)):

        if not self._parent:
            return 'no parent'

        child = self
        parent = self._parent
        exploitation_term = child.get_total_reward()/child.get_visit_count()
        exploration_term = exploration_factor*math.sqrt((2*math.log(parent.get_visit_count()))/child.get_visit_count())
        return round(exploitation_term + exploration_term, 4)

    def __str__(self):
        return 'holi'
    
    def __repr__(self):
        return f"<Node actn: {self._incoming_action} Val:{self.uct_val()} Rwrd: {self._total_reward}  Vists: {self._visit_count} Plyr:{self._state._player}>"



    
class GameState:
    def get_possible_actions(self):
        pass
    def next_state_from_action(self):
        pass
    def calculate_reward(self):
        pass
    def is_terminal(self):
        pass



