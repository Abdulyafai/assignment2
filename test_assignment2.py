import unittest
from assignment2 import bodymass
from assignment2 import retirement

class TestAssignment2(unittest.TestCase):

    def test_bodymass(self):
        self.assertEqual(bodymass(1,1), 4.882423653736196)
        self.assertEqual(bodymass(0,1), "pounds should be between 1 and 400")
        self.assertEqual(bodymass(1,0), "Height need to be between 1 and 8")

    def test_retirement(self):
        self.assertEqual(retirement(0,1,2,3), "Age cannot be 0")
        self.assertEqual(retirement(2,2,0,20), "Percentage should be between 0 and 100")
        self.assertEqual(retirement(101,2,2,2) ,"You cannot live over 100 years")
        self.assertEqual(retirement(2,0,2,2), "Salary cannot be 0 or less")
        self.assertEqual(retirement(25,100000,30,10000000), "you will die before you meet your goal, you'll meet your goal when you are (358.33) years old")
        self.assertEqual(retirement(25,100000,30,1000000) ,"58.33")





if __name__ == '__main__':
    unittest.main()