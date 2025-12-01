from main import calc_antinodes, in_bounds, calc_antinodes_with_resonance, calc_slope

import unittest

class Test(unittest.TestCase): 

	def test_calc_antinodes(self): 
		# vertical line
		self.assertCountEqual([(4,4), (4,16)], calc_antinodes((4,8), (4,12)))
		self.assertCountEqual([(4,4), (4,16)], calc_antinodes((4,12), (4,8)))

		# horizontal line
		self.assertCountEqual([(-4,8), (20,8)], calc_antinodes((4,8), (12,8)))
		self.assertCountEqual([(-4,8), (20,8)], calc_antinodes((12,8), (4,8)))

		# positive slope
		self.assertCountEqual([(4,0), (16,24)], calc_antinodes((8,8), (12,16)))
		self.assertCountEqual([(4,0), (16,24)], calc_antinodes((12,16), (8,8)))

		# negative slope
		self.assertCountEqual([(16,0), (4,12)], calc_antinodes((8,8), (12,4)))
		self.assertCountEqual([(16,0), (4,12)], calc_antinodes((12,4), (8,8)))

	def test_calc_antinodes_with_resonance(self): 	
		# vertical line
		self.assertCountEqual([(1,0), (1,1), (1,2), (1,3)], calc_antinodes_with_resonance((1,1), (1,3), 4, 4))
		self.assertCountEqual([(1,0), (1,1), (1,2), (1,3)], calc_antinodes_with_resonance((1,3), (1,1), 4, 4))
	
		# horizontal line
		self.assertCountEqual([(2,0), (2,1), (2,2), (2,3)], calc_antinodes_with_resonance((2,1), (2,3), 4, 4))
		self.assertCountEqual([(2,0), (2,1), (2,2), (2,3)], calc_antinodes_with_resonance((2,3), (2,1), 4, 4))

		# positive slope
		self.assertCountEqual([(0,0), (1,1), (2,2), (3,3)], calc_antinodes_with_resonance((1,1), (3,3), 4, 4))
		self.assertCountEqual([(0,0), (1,1), (2,2), (3,3)], calc_antinodes_with_resonance((3,3), (1,1), 4, 4))

		# negative slope
		self.assertCountEqual([(0,3), (1,2), (2,1), (3,0)], calc_antinodes_with_resonance((1,2), (2,1), 4, 4))
		self.assertCountEqual([(0,3), (1,2), (2,1), (3,0)], calc_antinodes_with_resonance((2,1), (1,2), 4, 4))

		#self.assertCountEqual([(0,3), (1,2), (2,1), (3,0)], calc_antinodes_with_resonance((7,8), (4,7), 12, 12))

	def test_in_bounds(self):
		self.assertTrue(in_bounds(0,0,2,2))
		self.assertTrue(in_bounds(0,1,2,2))
		self.assertTrue(in_bounds(1,0,2,2))
		self.assertTrue(in_bounds(1,1,2,2))

		self.assertFalse(in_bounds(-1,0,2,2))
		self.assertFalse(in_bounds(0,-1,2,2))
		self.assertFalse(in_bounds(-1,-1,2,2))
		self.assertFalse(in_bounds(2,0,2,2))
		self.assertFalse(in_bounds(0,2,2,2))
		self.assertFalse(in_bounds(2,2,2,2))
		self.assertFalse(in_bounds(-1,2,2,2))
		self.assertFalse(in_bounds(2,-1,2,2))
	
	def test_calc_slope(self):
		self.assertEqual((0,1), calc_slope(0,0,0,1))
		self.assertEqual((1,2), calc_slope(0,0,3,6))
		self.assertEqual((1,1), calc_slope(0,0,1,1))
		self.assertEqual((2,1), calc_slope(0,0,6,3))
		self.assertEqual((1,0), calc_slope(0,0,1,0))
		self.assertEqual((1,-1), calc_slope(0,0,1,-1))
		self.assertEqual((0,-1), calc_slope(0,0,0,-1))
		self.assertEqual((-1,-1), calc_slope(0,0,-1,-1))
		self.assertEqual((-1, 0), calc_slope(0,0,-1,0))
		self.assertEqual((-1, 1), calc_slope(0,0,-1,1))

		

if __name__ == '__main__':
    unittest.main()
