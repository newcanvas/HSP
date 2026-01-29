import unittest
from task4_code import Stack
from task4_text import Stack_tail
from task4_2 import isBalanced, returnMin, returnAvg, solve_postfix


class DivTests(unittest.TestCase):

    # Тесты для стека, работающего с хвостом.
    # pop()

    def test_tail_pop_empty(self):
        stack = Stack_tail()
        self.assertEqual(stack.pop(), None)

    def test_tail_pop_one(self):
        stack = Stack_tail()
        stack.push(99)
        self.assertEqual(stack.pop(), 99)
        self.assertEqual(stack.size(), 0)

    def test_tail_pop_several(self):
        stack = Stack_tail()
        for i in range(5):
            stack.push(i)
        self.assertEqual(stack.pop(), 4)
        self.assertEqual(stack.pop(), 3)
        self.assertEqual(stack.pop(), 2)
        self.assertEqual(stack.size(), 2)

    # push()
        
    def test_tail_push_one(self):
        stack = Stack_tail()
        stack.push(99)
        self.assertEqual(stack.pop(), 99)
        self.assertEqual(stack.size(), 0)

    def test_tail_push_several(self):
        stack = Stack_tail()
        for i in range(5):
            stack.push(i)
        self.assertEqual(stack.pop(), 4)
        self.assertEqual(stack.size(), 4)

    # peek()

    def test_tail_peek_empty(self):
        stack = Stack_tail()
        self.assertEqual(stack.peek(), None)

    def test_tail_peek_one(self):
        stack = Stack_tail()
        stack.push(99)
        self.assertEqual(stack.peek(), 99)
        self.assertEqual(stack.size(), 1)

    def test_tail_peek_several(self):
        stack = Stack_tail()
        for i in range(5):
            stack.push(i)
        self.assertEqual(stack.peek(), 4)
        self.assertEqual(stack.size(), 5)

    # size()

    def test_head_size_several(self):
        stack = Stack_tail()
        for i in range(5):
            stack.push(i)
        self.assertEqual(stack.size(), 5)

    def test_head_size_empty(self):
        stack = Stack_tail()
        self.assertEqual(stack.size(), 0)

    # Тесты для стека, работающего с головой
    # pop()

    def test_head_pop_empty(self):
        stack = Stack()
        self.assertEqual(stack.pop(), None)

    def test_head_pop_one(self):
        stack = Stack()
        stack.push(99)
        self.assertEqual(stack.pop(), 99)
        self.assertEqual(stack.size(), 0)

    def test_head_pop_several(self):
        stack = Stack()
        for i in range(5):
            stack.push(i)
        self.assertEqual(stack.pop(), 4)
        self.assertEqual(stack.pop(), 3)
        self.assertEqual(stack.pop(), 2)
        self.assertEqual(stack.size(), 2)

    # push()
        
    def test_head_push_one(self):
        stack = Stack()
        stack.push(99)
        self.assertEqual(stack.pop(), 99)
        self.assertEqual(stack.size(), 0)

    def test_head_push_several(self):
        stack = Stack()
        for i in range(5):
            stack.push(i)
        self.assertEqual(stack.pop(), 4)
        self.assertEqual(stack.size(), 4)

    # peek()

    def test_head_peek_empty(self):
        stack = Stack()
        self.assertEqual(stack.peek(), None)

    def test_head_peek_one(self):
        stack = Stack()
        stack.push(99)
        self.assertEqual(stack.peek(), 99)
        self.assertEqual(stack.size(), 1)

    def test_head_peek_several(self):
        stack = Stack()
        for i in range(5):
            stack.push(i)
        self.assertEqual(stack.peek(), 4)
        self.assertEqual(stack.size(), 5)
        
    # 5.
        
    def test_balance_empty(self):
        balance = isBalanced('')
        self.assertEqual(balance, None)

    def test_balance_mono_true(self):
        balance = isBalanced('()()((()))')
        self.assertEqual(balance, True)

    def test_balance_mono_false(self):
        balance = isBalanced('()()()))')
        self.assertEqual(balance, False)

    def test_balance_many_true(self):
        balance = isBalanced('()()((({[]}[])))')
        self.assertEqual(balance, True)

    def test_balance_many_false(self):
        balance = isBalanced('()([]){{({}})))')
        self.assertEqual(balance, False)

    # 7.
        
    def test_min_empty(self):
        stack = Stack()
        min_n = returnMin(stack)
        self.assertEqual(min_n, None)

    def test_min_several(self):
        stack = Stack()
        for i in range(5):
            stack.push(i)
        min_n = returnMin(stack)
        self.assertEqual(min_n, 0)

    def test_min_several_2(self):
        stack = Stack()
        for i in range(-100, 5):
            stack.push(i)
        stack.push(-1000)
        min_n = returnMin(stack)
        self.assertEqual(min_n, -1000)

    def test_min_several_types(self):
        stack = Stack()
        for i in range(-100, 5):
            stack.push(i)
        stack.push('asb')
        min_n = returnMin(stack)
        self.assertEqual(min_n, -100)

    # 8.
        
    def test_avg_empty(self):
        stack = Stack()
        avg_n = returnAvg(stack)
        self.assertEqual(avg_n, None)

    def test_avg_several(self):
        stack = Stack()
        for i in range(5):
            stack.push(i)
        avg_n = returnAvg(stack)
        self.assertEqual(avg_n, 2)

    def test_avg_several_2(self):
        stack = Stack()
        for i in range(-100, 5):
            stack.push(i)
        stack.push(-1000)
        avg_n = round(returnAvg(stack), 2)
        self.assertEqual(avg_n, -56.98)

    def test_avg_several_2(self):
        stack = Stack()
        for i in range(-100, 5):
            stack.push(i)
        stack.push(-1000)
        stack.push('fhdfhh')
        avg_n = round(returnAvg(stack), 2)
        self.assertEqual(avg_n, -56.45)

    # 9.
        
    def test_postfix_empty(self):
        solution = solve_postfix('')
        self.assertEqual(solution, None)

    def test_postfix_expression(self):
        solution = solve_postfix('8 2 + 5 * 9 + =')
        self.assertEqual(solution, 59)

    def test_postfix_expression_2(self):
        solution = solve_postfix('1 2 + 3 * =')
        self.assertEqual(solution, 9)

    def test_postfix_expression_3(self):
        solution = solve_postfix('1 1 2 + 4 * + =')
        self.assertEqual(solution, 13)
    
    

if __name__ == '__main__':
    unittest.main()
