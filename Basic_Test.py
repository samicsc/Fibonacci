import unittest
import fibonacci

class Testing(unittest.TestCase):
    def test_A(self):
        wanted_result = [0, 1, 1, 2, 3]
        test_result = fibonacci.fib2(5)
        self.assertEqual(wanted_result, test_result)
    
    def test_B(self):
        wanted_result = []
        test_result = fibonacci.fib2(0)
        self.assertEqual(wanted_result, test_result)

    def test_C(self):
        wanted_result = [0]
        test_result = fibonacci.fib2(1)
        self.assertEqual(wanted_result, test_result)

if __name__ == '__main__':
    unittest.main()