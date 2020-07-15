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
        self._visit_count = 0
        self._total_reward = 0
        self._parent = parent
        

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
        self._total_reward += reward

    def is_fully_expanded(self):
        return len(self._actions) == 0
    
    def get_children(self):
        return self._children

    # def check_rows(self):
    #     for row in self.state :
    #         if all_elements_equal(row):
    #             return True
    #     return False

    # def check_columns(self):
    #     transpose = list(zip(*self.state)) 
    #     for row in transpose :
    #         if all_elements_equal(row):
    #             return True
    #     return False

    # def all_elements_equal(self, list):
    #     iterator = iter(list)
    #     try:
    #         first = next(iterator)
    #     except StopIteration:
    #         return True
    #     return all(first == rest for rest in iterator)



    
class GameState:
    def get_possible_actions(self):
        pass
    def next_state_from_action(self):
        pass
    def calculate_reward(self):
        pass
    def is_terminal(self):
        pass



