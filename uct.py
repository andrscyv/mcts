import math
from node import Node
import random
# Each node has:
# - state (calculated instead of stored ?)
# - incoming action 
# - total simulation reward 
# - visit count 

def uct_decision(s0, num_iterations = 100):
    root = Node(None,state=s0)

    for i in range(0, num_iterations):
        node_to_expand = tree_policy(root)
        reward = default_policy(node_to_expand) 
        backup(node_to_expand, reward)
    
    return best_child(root, 0).get_incoming_action()

def tree_policy(node, exploration_factor = 1/pow(2,1/2)):

    while not node.is_terminal() :
        if not node.is_fully_expanded() :
            return expand(node)
        else:
            node = best_child(node, exploration_factor)

    return node

def expand(node):
    next_action = node.pop_action()
    new_node = Node(node,incoming_action=next_action)
    node.append_child(new_node)

    return new_node

def uct_val(parent, child, exploration_factor):
    exploitation_term = child.get_total_reward()/child.get_visit_count()
    exploration_term = exploration_factor*math.sqrt((2*math.log(parent.get_visit_count()))/child.get_visit_count())
    return exploitation_term + exploration_term
    
def best_child(node, exploration_factor):

    children_uct_value = [ uct_val(node, child, exploration_factor) for child in node.get_children() ]
    return node.get_children()[children_uct_value.index(max(children_uct_value))]

def default_policy(node):
    while not node.is_terminal():
        action = select_action(node) #random.choice(node.actions())
        node = Node(node,incoming_action=action)

    return node.calculate_reward()

def select_action(node):
    children = [ Node(node,incoming_action=action) for action in node.actions()]
    
    for node in children:
        if node.is_terminal():
            return node.get_incoming_action()

    return random.choice(node.actions())

def backup(node, reward):
    while node:
        node.register_visit(reward)
        node = node.get_parent()