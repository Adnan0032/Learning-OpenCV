from test10 import adder,mult,add_mult
import unittest

class test(unittest.TestCase):

    def test_add(self):
        result=adder(2,5)
        self.assertEqual(result,7)
        print("test is okk!!")
    
    def test_mul(self):
        result=mult(4,4)
        self.assertEqual(result,16)
        print("test 2 is okk!!")
    def test_add_and_multiply_positive(self):
        result = add_mult(2, 3, 4)
        self.assertEqual(result, 20)
        print("the test 3 is good!! well done") 

    def test_add_and_multiply_negative(self):
        result = add_mult(-2, 5, 2)
        self.assertEqual(result, 6)
        print("the test 4 is good!! well done")  

    def test_add_and_multiply_zero(self):
        result = add_mult(0, 0, 10)
        self.assertEqual(result, 0)
        print("the test 5 is good!! well done")   


if __name__ == '__main__':
    unittest.main()