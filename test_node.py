import unittest
from unittest import mock
from node import Node 
from node import GameState


class TestNode(unittest.TestCase):

    def test_create_node_from_state(self):
        state = GameState()
        root = Node(None, state=state)
        self.assertIsNotNone(root)
        self.assertIsNotNone(root._state)

    def test_create_node_from_incoming_action(self):
        state = mock.Mock()
        state.get_possible_actions.return_value = [1, 2]
        root = Node(None, state=state)
        node = Node(root, incoming_action=root.pop_action())
        self.assertIsNotNone(node)
        self.assertIsNotNone(node._state)
        self.assertTrue(state.next_state_from_action.called)

    def test_node_is_terminal_calls_state(self):
        state = mock.Mock()
        node = Node(None, state = state)
        node.is_terminal()  
        self.assertTrue(state.is_terminal.called)

    def test_is_fully_expanded(self):
        state = mock.Mock()
        state.get_possible_actions.return_value = [1, 2]
        node = Node(None, state = state)
        self.assertFalse(node.is_fully_expanded())

    def test_pop_action(self):
        state = mock.Mock(spec=GameState)
        state.get_possible_actions.return_value = [2,1] 
        node = Node(None, state=state)
        self.assertEqual(node.pop_action(), 1)

    def test_pop_action_empty(self):
        state = mock.Mock(spec=GameState)
        state.get_possible_actions.return_value = [] 
        node = Node(None, state=state)
        self.assertRaises(AssertionError, node.pop_action)

    def test_append_child(self):
        state = mock.Mock(spec=GameState)
        state.get_possible_actions.return_value = [1, 2]
        node = Node(None, state=state)
        incoming_action = node.pop_action()
        child_node = Node(node, incoming_action=incoming_action)
        node.append_child(child_node)
        self.assertTrue(child_node in node.get_children())

    def test_calculate_reward(self):
        state = mock.Mock(spec=GameState)
        node = Node(None, state=state)
        node.calculate_reward()
        self.assertTrue(state.calculate_reward.called)

    def test_register_visit(self):
        state = mock.Mock(spec=GameState)
        node = Node(None, state=state)
        self.assertEqual(node._visit_count, 0)
        self.assertEqual(node._total_reward, 0)
        node.register_visit(5)
        self.assertEqual(node._visit_count, 1)
        self.assertEqual(node._total_reward,5)


