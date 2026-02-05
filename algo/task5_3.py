import unittest

from task5 import Queue, Node
from task5_2 import Queue_2, Queue_3, rotateQueue, reverseQueue

class DivTests(unittest.TestCase):

    # 1.

    def test_enqueue_dequeue_one(self):
        queue1 =  Queue()
        queue1.enqueue(Node(10))
        self.assertEqual(queue1.size(), 1)
        self.assertEqual(queue1.dequeue(), 10)
        self.assertEqual(queue1.size(), 0)

    def test_dequeue_empty(self):
        queue1 =  Queue()
        self.assertIsNone(queue1.dequeue())
        self.assertEqual(queue1.size(), 0)

    def test_multiple(self):
        queue1 =  Queue()
        queue1.enqueue(Node(1))
        queue1.enqueue(Node(2))
        queue1.enqueue(Node(3))
        self.assertEqual(queue1.dequeue(), 1)
        self.assertEqual(queue1.dequeue(), 2)
        self.assertEqual(queue1.dequeue(), 3)
        self.assertEqual(queue1.size(), 0)

    def test_borders_queue(self):
        queue1 =  Queue()
        queue1.enqueue(Node(42))
        queue1.dequeue()
        self.assertIsNone(queue1.head)
        self.assertIsNone(queue1.tail)
        self.assertEqual(queue1.size(), 0)

    # 3.

    def test_rotate_empty_queue(self):
        queue1 =  Queue()
        rotateQueue(queue1, 3)
        self.assertEqual(queue1.size(), 0)
        self.assertIsNone(queue1.head)
        self.assertIsNone(queue1.tail)

    def test_rotate_one_element(self):
        queue1 =  Queue()
        queue1.enqueue(Node(10))
        rotateQueue(queue1, 5)
        self.assertEqual(queue1.size(), 1)
        self.assertEqual(queue1.dequeue(), 10)
        self.assertEqual(queue1.size(), 0)

    def test_rotate_one_step(self):
        queue1 =  Queue()
        queue1.enqueue(Node(1))
        queue1.enqueue(Node(2))
        queue1.enqueue(Node(3))
        rotateQueue(queue1, 1)
        self.assertEqual(queue1.dequeue(), 2)
        self.assertEqual(queue1.dequeue(), 3)
        self.assertEqual(queue1.dequeue(), 1)

    def test_rotate_several_steps(self):
        queue1 =  Queue()
        queue1.enqueue(Node(1))
        queue1.enqueue(Node(2))
        queue1.enqueue(Node(3))
        rotateQueue(queue1, 4)
        self.assertEqual(queue1.dequeue(), 2)
        self.assertEqual(queue1.dequeue(), 3)
        self.assertEqual(queue1.dequeue(), 1)

    # 4.

    def test_enqueue_dequeue_one_stacks(self):
        queue1 =  Queue_2()
        queue1.enqueue(10)
        self.assertEqual(queue1.size(), 1)
        self.assertEqual(queue1.dequeue(), 10)
        self.assertEqual(queue1.size(), 0)

    def test_dequeue_empty_stacks(self):
        queue1 =  Queue_2()
        self.assertIsNone(queue1.dequeue())
        self.assertEqual(queue1.size(), 0)

    def test_multiple_stacks(self):
        queue1 =  Queue_2()
        queue1.enqueue(1)
        queue1.enqueue(2)
        queue1.enqueue(3)
        self.assertEqual(queue1.dequeue(), 1)
        self.assertEqual(queue1.dequeue(), 2)
        self.assertEqual(queue1.dequeue(), 3)
        self.assertEqual(queue1.size(), 0)

    def test_multiple_stacks_2(self):
        queue1 =  Queue()
        queue1.enqueue(Node(1))
        self.assertEqual(queue1.dequeue(), 1)
        queue1.enqueue(Node(2))
        queue1.enqueue(Node(3))
        self.assertEqual(queue1.dequeue(), 2)
        queue1.enqueue(Node(4))
        self.assertEqual(queue1.dequeue(), 3)
        self.assertEqual(queue1.dequeue(), 4)
        self.assertEqual(queue1.size(), 0)

    # 5.

    def test_reverse_empty_queue(self):
        queue1 =  Queue()
        result = reverseQueue(queue1)
        self.assertIsNone(result)
        self.assertEqual(queue1.size(), 0)

    def test_reverse_one(self):
        queue1 =  Queue()
        queue1.enqueue(Node(10))
        reverseQueue(queue1)
        self.assertEqual(queue1.dequeue(), 10)
        self.assertEqual(queue1.size(), 0)

    def test_reverse_multipl(self):
        queue1 =  Queue()
        queue1.enqueue(Node(1))
        queue1.enqueue(Node(2))
        queue1.enqueue(Node(3))
        reverseQueue(queue1)
        self.assertEqual(queue1.dequeue(), 3)
        self.assertEqual(queue1.dequeue(), 2)
        self.assertEqual(queue1.dequeue(), 1)
        self.assertEqual(queue1.size(), 0)

    def test_reverse_twice(self):
        queue1 =  Queue()
        queue1.enqueue(Node(1))
        queue1.enqueue(Node(2))
        queue1.enqueue(Node(3))
        reverseQueue(queue1)
        reverseQueue(queue1)
        self.assertEqual(queue1.dequeue(), 1)
        self.assertEqual(queue1.dequeue(), 2)
        self.assertEqual(queue1.dequeue(), 3)
        self.assertEqual(queue1.size(), 0)

    # 6.

    def test_enqueue_dequeue(self):
        queue1 =  Queue_3()
        queue1.enqueue(1)
        queue1.enqueue(2)
        queue1.enqueue(3)
        self.assertEqual(queue1.dequeue(), 1)
        self.assertEqual(queue1.dequeue(), 2)
        self.assertEqual(queue1.dequeue(), 3)
        self.assertEqual(queue1.size(), 0)

    def test_dequeue_from_empty_queue(self):
        queue1 =  Queue_3()
        self.assertIsNone(queue1.dequeue())
        self.assertEqual(queue1.size(), 0)

    def test_enqueue_full(self):
        queue1 =  Queue_3()
        queue1.enqueue(1)
        queue1.enqueue(2)
        queue1.enqueue(3)
        queue1.enqueue(4)
        queue1.enqueue(5)
        self.assertEqual(queue1.size(), 5)
        with self.assertRaises(Exception):
            queue1.enqueue(6)

    def test_circular_behavior_after_wrap(self):
        queue1 =  Queue_3()
        queue1.enqueue(1)
        queue1.enqueue(2)
        queue1.enqueue(3)
        queue1.dequeue()
        queue1.dequeue()
        queue1.enqueue(4)
        queue1.enqueue(5)
        self.assertEqual(queue1.dequeue(), 3)
        self.assertEqual(queue1.dequeue(), 4)
        self.assertEqual(queue1.dequeue(), 5)
        self.assertEqual(queue1.size(), 0)

if __name__ == '__main__':
    unittest.main()

