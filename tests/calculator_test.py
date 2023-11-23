import unittest
from calculator import add, subtract, mult, div

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(3, 4), 7)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(5, 3), 8)
        self.assertEqual(add(0, 0), 0)
        self.assertEqual(add(10, -5), 5)

    def test_subtract(self):
        self.assertEqual(subtract(8, 3), 5)
        self.assertEqual(subtract(5, 5), 0)
        self.assertEqual(subtract(5, -5), 10)
        self.assertEqual(subtract(0, -1), -1)
        self.assertEqual(subtract(-10, 2), -8)
        
    def test_multiply(self):
        self.assertEqual(mult(2, 2), 4)
        self.assertEqual(mult(0, 9), 0)
        self.assertEqual(mult(10, -1), -10)
        self.assertEqual(mult(-3, -2), 6)
        self.assertEqual(mult(0, 0), 0)

    def test_div(self):
        self.assertEqual(div(2, 2), 1)
        self.assertEqual(div(0, 10), 0)
        self.assertEqual(div(6, 4), 1.5)
        self.assertEqual(div(5, 2), 2.5)
        self.assertEqual(div(9, 0), "Error! Divide by zero!")

if __name__ == '__main__':
    unittest.main()
