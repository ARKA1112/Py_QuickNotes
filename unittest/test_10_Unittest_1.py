import unittest
import calc



class TestCalc(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calc.add(1,3),4)



if __name__ == '__main__':
    unittest.main()