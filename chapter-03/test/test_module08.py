import unittest
import test_me

class TestClass09(unittest.TestCase):
    def test_case01(self):
        self.assertEqual(test_me.add(2,3), 5)

    def test_case02(self):
        self.assertEqual(test_me.mul(2,3), 6)
