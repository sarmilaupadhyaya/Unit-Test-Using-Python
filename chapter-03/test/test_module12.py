import sys
import unittest

class TestClass13(unittest.TestCase):

    @unittest.skip("demonstrating unconditional skipping")
    def test_case01(self):
        self.fail("FATAL")

    @unittest.skipUnless(sys.platform.startswith("win"), "requires Windows")
    def test_case02(self):
        ## window specific test code
        pass

    @unittest.skipUnless(sys.platform.startswith("linux"), "requires linux")
    def test_case03(self):
        # Linux specific testing code
        pass
