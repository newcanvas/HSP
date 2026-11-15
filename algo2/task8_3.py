import unittest

from task8 import SimpleGraph, Vertex
from task8_2 import DirectedGraph


def make_graph(size, values):
    graph = SimpleGraph(size)
    for value in values:
        graph.AddVertex(value)
    return graph


def make_directed(size, values):
    graph = DirectedGraph(size)
    for value in values:
        graph.AddVertex(value)
    return graph


class TestAddVertex(unittest.TestCase):

    def test_add_vertex_to_empty_graph(self):
        graph = SimpleGraph(3)

        graph.AddVertex(5)

        self.assertIsInstance(graph.vertex[0], Vertex)
        self.assertEqual(graph.vertex[0].Value, 5)

    def test_add_vertex_creates_no_edges(self):
        graph = SimpleGraph(3)

        graph.AddVertex(5)

        self.assertEqual(graph.m_adjacency, [[0, 0, 0], [0, 0, 0], [0, 0, 0]])

    def test_add_vertex_fills_first_free_slot(self):
        graph = make_graph(4, [1, 2])

        graph.RemoveVertex(0)
        graph.AddVertex(3)

        self.assertEqual(graph.vertex[0].Value, 3)
        self.assertEqual(graph.vertex[1].Value, 2)

    def test_add_vertex_fills_graph(self):
        graph = make_graph(2, [1, 2])

        self.assertEqual(graph.vertex[0].Value, 1)
        self.assertEqual(graph.vertex[1].Value, 2)
        self.assertNotIn(None, graph.vertex)

    def test_add_vertex_to_full_graph(self):
        graph = make_graph(1, [1])

        graph.AddVertex(2)

        self.assertEqual(graph.vertex[0].Value, 1)
        self.assertEqual(len(graph.vertex), 1)


class TestIsEdge(unittest.TestCase):

    def test_no_edges_in_new_graph(self):
        graph = make_graph(3, [1, 2, 3])

        self.assertFalse(graph.IsEdge(0, 1))
        self.assertFalse(graph.IsEdge(1, 0))
        self.assertFalse(graph.IsEdge(2, 2))

    def test_edge_appears_after_add(self):
        graph = make_graph(2, [1, 2])

        graph.AddEdge(0, 1)

        self.assertTrue(graph.IsEdge(0, 1))
        self.assertTrue(graph.IsEdge(1, 0))

    def test_self_loop(self):
        graph = make_graph(1, [1])

        graph.AddEdge(0, 0)

        self.assertTrue(graph.IsEdge(0, 0))

    def test_edge_of_removed_vertex(self):
        graph = make_graph(2, [1, 2])
        graph.AddEdge(0, 1)

        graph.RemoveVertex(1)

        self.assertFalse(graph.IsEdge(0, 1))
        self.assertFalse(graph.IsEdge(1, 0))


class TestAddEdge(unittest.TestCase):

    def test_add_edge_before_and_after(self):
        graph = make_graph(2, [1, 2])

        self.assertFalse(graph.IsEdge(0, 1))

        graph.AddEdge(0, 1)

        self.assertTrue(graph.IsEdge(0, 1))

    def test_edge_is_symmetric(self):
        graph = make_graph(2, [1, 2])

        graph.AddEdge(0, 1)

        self.assertEqual(graph.m_adjacency[0][1], 1)
        self.assertEqual(graph.m_adjacency[1][0], 1)

    def test_add_same_edge_twice(self):
        graph = make_graph(2, [1, 2])

        graph.AddEdge(0, 1)
        graph.AddEdge(0, 1)

        self.assertEqual(graph.m_adjacency[0][1], 1)
        self.assertEqual(graph.m_adjacency[1][0], 1)

    def test_complete_graph(self):
        graph = make_graph(3, [1, 2, 3])

        graph.AddEdge(0, 1)
        graph.AddEdge(0, 2)
        graph.AddEdge(1, 2)

        for i in range(3):
            for j in range(3):
                if i != j:
                    self.assertTrue(graph.IsEdge(i, j))


class TestRemoveEdge(unittest.TestCase):

    def test_remove_edge_before_and_after(self):
        graph = make_graph(2, [1, 2])
        graph.AddEdge(0, 1)

        self.assertTrue(graph.IsEdge(0, 1))

        graph.RemoveEdge(0, 1)

        self.assertFalse(graph.IsEdge(0, 1))

    def test_remove_edge_is_symmetric(self):
        graph = make_graph(2, [1, 2])
        graph.AddEdge(0, 1)

        graph.RemoveEdge(0, 1)

        self.assertEqual(graph.m_adjacency[0][1], 0)
        self.assertEqual(graph.m_adjacency[1][0], 0)

    def test_remove_absent_edge(self):
        graph = make_graph(2, [1, 2])

        graph.RemoveEdge(0, 1)

        self.assertFalse(graph.IsEdge(0, 1))

    def test_remove_only_one_edge(self):
        graph = make_graph(3, [1, 2, 3])
        graph.AddEdge(0, 1)
        graph.AddEdge(1, 2)

        graph.RemoveEdge(0, 1)

        self.assertFalse(graph.IsEdge(0, 1))
        self.assertTrue(graph.IsEdge(1, 2))


class TestRemoveVertex(unittest.TestCase):

    def test_remove_vertex_clears_its_edges(self):
        graph = make_graph(3, [1, 2, 3])
        graph.AddEdge(0, 1)
        graph.AddEdge(0, 2)

        self.assertTrue(graph.IsEdge(0, 1))
        self.assertTrue(graph.IsEdge(0, 2))

        graph.RemoveVertex(0)

        self.assertIsNone(graph.vertex[0])

        for index in range(3):
            self.assertEqual(graph.m_adjacency[0][index], 0)
            self.assertEqual(graph.m_adjacency[index][0], 0)

    def test_remove_vertex_keeps_other_edges(self):
        graph = make_graph(3, [1, 2, 3])
        graph.AddEdge(0, 1)
        graph.AddEdge(1, 2)

        graph.RemoveVertex(0)

        self.assertTrue(graph.IsEdge(1, 2))
        self.assertFalse(graph.IsEdge(1, 0))

    def test_remove_isolated_vertex(self):
        graph = make_graph(3, [1, 2, 3])
        graph.AddEdge(0, 1)

        graph.RemoveVertex(2)

        self.assertIsNone(graph.vertex[2])
        self.assertTrue(graph.IsEdge(0, 1))

    def test_remove_vertex_frees_slot(self):
        graph = make_graph(2, [1, 2])

        graph.RemoveVertex(1)

        self.assertIsNone(graph.vertex[1])
        self.assertEqual(graph.vertex[0].Value, 1)

    def test_add_vertex_reuses_freed_slot(self):
        graph = make_graph(2, [1, 2])

        graph.RemoveVertex(0)
        graph.AddVertex(9)

        self.assertEqual(graph.vertex[0].Value, 9)
        self.assertEqual(len(graph.vertex), 2)


class TestDirectedGraph(unittest.TestCase):

    def test_edge_is_directed(self):
        graph = make_directed(2, [1, 2])

        graph.AddEdge(0, 1)

        self.assertTrue(graph.IsEdge(0, 1))
        self.assertFalse(graph.IsEdge(1, 0))

    def test_remove_directed_edge(self):
        graph = make_directed(2, [1, 2])
        graph.AddEdge(0, 1)

        graph.RemoveEdge(0, 1)

        self.assertFalse(graph.IsEdge(0, 1))
        self.assertFalse(graph.IsEdge(1, 0))

    def test_remove_edge_does_not_touch_reverse(self):
        graph = make_directed(2, [1, 2])
        graph.AddEdge(0, 1)
        graph.AddEdge(1, 0)

        graph.RemoveEdge(0, 1)

        self.assertFalse(graph.IsEdge(0, 1))
        self.assertTrue(graph.IsEdge(1, 0))

    def test_empty_graph_is_acyclic(self):
        graph = make_directed(3, [1, 2, 3])

        self.assertFalse(graph.IsCyclic())

    def test_isolated_vertices_are_acyclic(self):
        graph = make_directed(3, [1, 2, 3])
        graph.AddEdge(0, 1)

        self.assertFalse(graph.IsCyclic())

    def test_chain_is_acyclic(self):
        graph = make_directed(4, [1, 2, 3, 4])
        graph.AddEdge(0, 1)
        graph.AddEdge(1, 2)
        graph.AddEdge(2, 3)

        self.assertFalse(graph.IsCyclic())

    def test_triangle_is_cyclic(self):
        graph = make_directed(3, [1, 2, 3])
        graph.AddEdge(0, 1)
        graph.AddEdge(1, 2)
        graph.AddEdge(2, 0)

        self.assertTrue(graph.IsCyclic())

    def test_two_vertex_cycle(self):
        graph = make_directed(2, [1, 2])
        graph.AddEdge(0, 1)
        graph.AddEdge(1, 0)

        self.assertTrue(graph.IsCyclic())

    def test_self_loop_is_cycle(self):
        graph = make_directed(2, [1, 2])
        graph.AddEdge(0, 0)

        self.assertTrue(graph.IsCyclic())

    def test_diamond_is_acyclic(self):
        graph = make_directed(4, [1, 2, 3, 4])
        graph.AddEdge(0, 1)
        graph.AddEdge(0, 2)
        graph.AddEdge(1, 3)
        graph.AddEdge(2, 3)

        self.assertFalse(graph.IsCyclic())

    def test_cycle_in_one_component_only(self):
        graph = make_directed(6, [1, 2, 3, 4, 5, 6])
        graph.AddEdge(0, 1)
        graph.AddEdge(1, 2)
        graph.AddEdge(3, 4)
        graph.AddEdge(4, 5)
        graph.AddEdge(5, 3)

        self.assertTrue(graph.IsCyclic())

    def test_after_removing_edge_graph_becomes_acyclic(self):
        graph = make_directed(3, [1, 2, 3])
        graph.AddEdge(0, 1)
        graph.AddEdge(1, 2)
        graph.AddEdge(2, 0)

        self.assertTrue(graph.IsCyclic())

        graph.RemoveEdge(2, 0)

        self.assertFalse(graph.IsCyclic())

    def test_removed_vertex_does_not_create_cycle(self):
        graph = make_directed(3, [1, 2, 3])
        graph.AddEdge(0, 1)
        graph.AddEdge(1, 2)
        graph.AddEdge(2, 0)

        graph.RemoveVertex(2)

        self.assertFalse(graph.IsCyclic())


if __name__ == '__main__':
    unittest.main()
