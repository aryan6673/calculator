import unittest
from calculator import ModernCalculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = ModernCalculator()

    def test_addition(self):
        # Add your tests here
        pass

if __name__ == '__main__':
    unittest.main()
