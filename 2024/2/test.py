from main import calc_safety, calc_safety_with_tolerance;
import unittest

class Test(unittest.TestCase): 
	def test_calc_dist(self): 
		self.assertEqual(True, calc_safety([7, 6, 4, 2, 1]))
		self.assertEqual(False, calc_safety([1, 2, 7, 8, 9]))
		self.assertEqual(False, calc_safety([9, 7, 6, 2, 1]))
		self.assertEqual(False, calc_safety([1, 3, 2, 4, 5]))
		self.assertEqual(False, calc_safety([8, 6, 4, 4, 1]))
		self.assertEqual(True, calc_safety([1, 3, 6, 7, 9]))

	def calc_safety_with_tolerance(self): 
		self.assertEqual(True, calc_safety_with_tolerance([7, 6, 4, 2, 1]))
		self.assertEqual(False, calc_safety_with_tolerance([1, 2, 7, 8, 9]))
		self.assertEqual(False, calc_safety_with_tolerance([9, 7, 6, 2, 1]))
		self.assertEqual(True, calc_safety_with_tolerance([1, 3, 2, 4, 5]))
		self.assertEqual(True, calc_safety_with_tolerance([8, 6, 4, 4, 1]))
		self.assertEqual(True, calc_safety_with_tolerance([1, 3, 6, 7, 9]))

if __name__ == '__main__':
    unittest.main()
