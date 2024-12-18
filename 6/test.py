from main import find_start_pos, in_bounds, fill_map, count_map, BLOCK_CHAR, START_CHAR, pretty_print

import unittest

class Test(unittest.TestCase): 
	simple_map = []
	simple_map_size = ()
	

	def setUp(self):
		self.simple_map = [
			['.','.',BLOCK_CHAR,'.','.',],
			['.','.','.','.',BLOCK_CHAR,],
			['.','.','.','.','.',],
			['.','.',START_CHAR,'.','.',],
			['.','.','.','.','.',],
			['.','.','.',BLOCK_CHAR,'.',],
		]	
		
		self.simple_map_size = (len(self.simple_map), len(self.simple_map[0]))

	def test_find_start_pos(self): 
		self.assertEqual((0,0), find_start_pos([[START_CHAR]]))
		self.assertEqual((3,2), find_start_pos(self.simple_map))

	def test_in_bounds(self): 
		self.assertEqual(True, in_bounds((0,0), self.simple_map_size))
		self.assertEqual(True, in_bounds((5,4), self.simple_map_size))
		self.assertEqual(True, in_bounds((3,2), self.simple_map_size))
		self.assertEqual(False, in_bounds((-1,2), self.simple_map_size))
		self.assertEqual(False, in_bounds((3,-1), self.simple_map_size))
		self.assertEqual(False, in_bounds((6,2), self.simple_map_size))
		self.assertEqual(False, in_bounds((3,5), self.simple_map_size))
		self.assertEqual(False, in_bounds((6,5), self.simple_map_size))

	def test_fill_map_simple(self): 
		fill_map(self.simple_map)
		
		pretty_print(self.simple_map)

		self.assertEqual([
			['.','.',BLOCK_CHAR,'.','.',],
			['.','.','X','X',BLOCK_CHAR,],
			['.','.','X','X','.',],
			['.','.','^','X','.',],
			['X','O','X','X','.',],
			['.','.','.',BLOCK_CHAR,'.',],
			], self.simple_map)
		
	def test_fill_map_complex(self):
		complex_map = [
			['.','.','.','.','#','.','.','.','.','.',],
			['.','.','.','.','.','.','.','.','.','#',],
			['.','.','.','.','.','.','.','.','.','.',],
			['.','.','#','.','.','.','.','.','.','.',],
			['.','.','.','.','.','.','.','#','.','.',],
			['.','.','.','.','.','.','.','.','.','.',],
			['.','#','.','.','^','.','.','.','.','.',],
			['.','.','.','.','.','.','.','.','#','.',],
			['#','.','.','.','.','.','.','.','.','.',],
			['.','.','.','.','.','.','#','.','.','.',],
		]

		fill_map(complex_map)
		
		self.assertEqual([
			['.', '.', '.', '.', '#', '.', '.', '.', '.', '.'],
			['.', '.', '.', '.', 'X', 'X', 'X', 'X', 'X', '#'],
			['.', '.', '.', '.', 'X', '.', '.', '.', 'X', '.'],
			['.', '.', '#', '.', 'X', '.', '.', '.', 'X', '.'],
			['.', '.', 'X', 'X', 'X', 'X', 'X', '#', 'X', '.'],
			['.', '.', 'X', '.', 'X', '.', 'X', '.', 'X', '.'],
			['.', '#', 'X', 'O', '^', 'X', 'X', 'X', 'X', '.'],
			['.', 'X', 'X', 'X', 'X', 'X', 'O', 'O', '#', '.'],
			['#', 'O', 'X', 'O', 'X', 'X', 'X', 'X', '.', '.'],
			['.', '.', '.', '.', '.', '.', '#', 'O', '.', '.'],
		], complex_map)

	def test_count_map(self): 
			self.assertEqual((3, 1), count_map(['#', 'X', 'O', '^']))
			self.assertEqual((10, 4), count_map([
				['.', '#', 'O', 'X'],
				['.', 'X', 'X', 'X'],
				['#', '^', 'O', '#'],
				['.', 'X', 'O', 'O'],
			]))
		
if __name__ == '__main__':
    unittest.main()
