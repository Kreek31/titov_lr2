import unittest
from functions import add, multiply


class TestCalc(unittest.TestCase):

  def test_add(self):
    self.assertEqual(add(2, 3), 5)
    self.assertEqual(add(-1, 1), 0)

  def test_multiply(self):
     self.assertEqual(multiply(1, 0), 0)
     self.assertEqual(multiply(1, 2), 2)
     self.assertEqual(multiply(2, 3), 6)


if __name__ == '__main__':
    unittest.main()