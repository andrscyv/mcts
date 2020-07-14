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