from main import calc_dist, calc_similarity;
import unittest


class Test(unittest.TestCase): 
    def test_calc_dist(self): 
        self.assertEqual(0, calc_dist([1], [1]))
        self.assertEqual(0, calc_dist([1, 2], [1, 2]))
        
        
        self.assertEqual(4, calc_dist([1, 3], [3, 1]))

    def test_calc_similarity(self): 
        self.assertEqual(2, calc_similarity([1], [1, 1]))
        self.assertEqual(0, calc_similarity([2], [1, 1]))

        self.assertEqual(31, calc_similarity([3, 4, 2, 1, 3, 3], [4, 3, 5, 3, 9, 3]))

if __name__ == '__main__':
    unittest.main()
