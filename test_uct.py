import unittest
import unittest.mock as mock
from uct import *
from node import Node
class UctTestCase(unittest.TestCase):

    @mock.patch('uct.best_child')
    @mock.patch('uct.backup')
    @mock.patch('uct.default_policy')
    @mock.patch('uct.tree_policy')
    @mock.patch('uct.Node')
    def test_uct(
        self,
        mock_node,
        mock_tree_policy,
        mock_default_policy,
        mock_backup,
        mock_best_child
    ):
        uct_decision({})
        self.assertTrue(mock_node.called)
        self.assertTrue(mock_tree_policy.called)
        self.assertEqual(100, mock_tree_policy.call_count)
        self.assertTrue(mock_default_policy.called)
        self.assertTrue(mock_backup.called)
        self.assertTrue(mock_best_child.called)

    @mock.patch('uct.best_child')
    @mock.patch('uct.backup')
    @mock.patch('uct.default_policy')
    @mock.patch('uct.tree_policy')
    @mock.patch('uct.Node')
    def test_uct(
        self,
        mock_node,
        mock_tree_policy,
        mock_default_policy,
        mock_backup,
        mock_best_child
    ):
        uct_decision({}, num_iterations=20)
        self.assertTrue(mock_node.called)
        self.assertTrue(mock_tree_policy.called)
        self.assertEqual(20, mock_tree_policy.call_count)
        self.assertTrue(mock_default_policy.called)
        self.assertTrue(mock_backup.called)
        self.assertTrue(mock_best_child.called)

    @mock.patch('uct.best_child')
    @mock.patch('uct.expand')
    def test_tree_policy_terminal_node(
        self,
        mock_expand,
        mock_best_child
    ):
        node = mock.Mock()
        node.is_terminal.return_value = True
        tree_policy(node)
        self.assertFalse(mock_expand.called)
        self.assertFalse(mock_best_child.called)

    @mock.patch('uct.best_child')
    @mock.patch('uct.expand')
    def test_tree_policy_node_fully_expanded(
        self,
        mock_expand,
        mock_best_child
    ):
        node = mock.Mock()
        node.is_terminal.side_effect = [False, True] 
        node.is_fully_expanded.return_value = False
        tree_policy(node)
        self.assertTrue(mock_expand.called)
        self.assertFalse(mock_best_child.called)

    @mock.patch('uct.best_child')
    @mock.patch('uct.expand')
    def test_tree_policy_node(
        self,
        mock_expand,
        mock_best_child
    ):
        node = mock.Mock()
        node.is_terminal.side_effect = [False, True] 
        node.is_fully_expanded.return_value = True
        tree_policy(node)
        self.assertFalse(mock_expand.called)
        self.assertTrue(mock_best_child.called)

    @mock.patch('uct.Node')
    def test_expand(self, mock_node):
        node = mock.Mock()
        node.pop_action.return_value = 1
        expand(node)
        self.assertTrue(node.append_child.called)
        self.assertTrue(node.pop_action.called)

    @mock.patch('uct.random')
    @mock.patch('uct.Node')
    def test_default_policy(self, mock_node, mock_random):
        node = mock.Mock()
        node.is_terminal.side_effect = [False, True]
        mock_random.choice.return_value =1
        child_node = mock.Mock()
        mock_node.return_value = child_node
        
        default_policy(node)
        self.assertTrue(child_node.calculate_reward.called)

    # def test_backup(self):
    #     node = mock.Mock()



    def test_uct_val(self):
        child_total_reward = 5 
        child_visit_count = 10
        exploration_factor = 1/pow(2,1/2)
        parent_visit_count = 20
        parent = mock.Mock(spec=Node)
        child = mock.Mock(spec=Node)

        parent.get_visit_count.return_value = parent_visit_count
        child.get_visit_count.return_value = child_visit_count
        child.get_total_reward.return_value = child_total_reward

        self.assertAlmostEqual(1.0473328, uct_val(parent, child, exploration_factor))

    def test_best_child(self):
        child_total_reward = 4 
        child_visit_count = 10 
        child2_total_reward = 8 
        exploration_factor = 1/pow(2,1/2)
        parent_visit_count = 20
        child2_visit_count = parent_visit_count - child_visit_count 
        parent = mock.Mock(spec=Node)
        child = mock.Mock(spec=Node)
        child2 = mock.Mock(spec=Node)

        parent.get_visit_count.return_value = parent_visit_count
        child.get_visit_count.return_value = child_visit_count
        child.get_total_reward.return_value = child_total_reward
        child2.get_visit_count.return_value = child2_visit_count
        child2.get_total_reward.return_value = child2_total_reward
        children_arr = [child, child2]
        parent.get_children.return_value = children_arr
        # print([ uct_val(parent, c, exploration_factor) for c in children_arr ])
        self.assertEqual(child2, best_child(parent, exploration_factor))
    



