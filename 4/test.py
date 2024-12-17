from main import find_neighbors, find_word, find_x_mas

import unittest

class Test(unittest.TestCase): 
	
	def test_find_neighbors(self): 
		self.assertEqual(3, len(find_neighbors(0, 0, 3)))
		self.assertEqual(5, len(find_neighbors(1, 0, 3)))
		self.assertEqual(3, len(find_neighbors(2, 0, 3)))
		self.assertEqual(5, len(find_neighbors(0, 1, 3)))
		self.assertEqual(8, len(find_neighbors(1, 1, 3)))
		self.assertEqual(5, len(find_neighbors(2, 1, 3)))
		self.assertEqual(3, len(find_neighbors(0, 2, 3)))
		self.assertEqual(5, len(find_neighbors(1, 2, 3)))
		self.assertEqual(3, len(find_neighbors(2, 2, 3)))


	def test_find_word(self): 
		self.assertEqual(2, find_word([
			"XMAS",
			"MFAS",
			"ADEV",
			"SSSS",
		], "XMAS"))
				
		self.assertEqual(18, find_word([
			"MMMSXXMASM",
			"MSAMXMSMSA",
			"AMXSXMAAMM",
			"MSAMASMSMX",
			"XMASAMXAMM",
			"XXAMMXXAMA",
			"SMSMSASXSS",
			"SAXAMASAAA",
			"MAMMMXMMMM",
			"MXMXAXMASX"
		], "XMAS")) 
	

	def test_find_x_mas(self): 
		self.assertEqual(1, find_x_mas([
			"M.S",
			".A.",
			"M.S",
		]))
				
if __name__ == '__main__':
    unittest.main()
