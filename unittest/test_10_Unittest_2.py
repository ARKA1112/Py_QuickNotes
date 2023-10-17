## Distinguishing test iterations using subtests
import unittest

class NumbersTest(unittest.TestCase):

    def test_even(self):
        """
        Test that numbers between 0 and 5 are all even
        """

        for i in range(0,5):
            with self.subTest(i=i):
                self.assertEqual(i%2,0)


if __name__ == '__main__':
    unittest.main()