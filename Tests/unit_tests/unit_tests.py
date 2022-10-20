# demo unittest module and class

# 1 -> import unittest and the module/class/fns to be tested
import unittest
from example_fn import add_nums

# 2 -> Make class that inherits from unittest.TestCase
# 3 -> Define each method to begin with test* & add assert property to the self instance


class ExampleTester(unittest.TestCase):
    def test_add_nums(self):
        """Ensure adding reaches correct value"""
        self.assertEqual(add_nums(2, 3), 5)

    def test_add_wrong(self):
        """Ensure value does not equal certain value"""
        self.assertNotEqual(add_nums(2, 3), 0)


# 4 -> run unittest.main() only if the test function is run
if __name__ == "__main__":
    unittest.main()
