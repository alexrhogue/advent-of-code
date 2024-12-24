from main import count_corners

import unittest

class Test(unittest.TestCase): 

	def test_count_corners(self):
		self.assertEqual(0, count_corners([
			['X','X','X'],
			['X','X','X'],
			['X','X','X'],
		]))

		self.assertEqual(1, count_corners([
			['-','X','X'],
			['X','X','X'],
			['X','X','X'],
		]))

		self.assertEqual(1, count_corners([
			['-','=','X'],
			['+','X','X'],
			['X','X','X'],
		]))
	
		self.assertEqual(1, count_corners([
			['X','X','-'],
			['X','X','X'],
			['X','X','X'],
		]))
	
		self.assertEqual(1, count_corners([
			['X','+','-'],
			['X','X','='],
			['X','X','X'],
		]))
	
		self.assertEqual(1, count_corners([
			['X','X','X'],
			['X','X','X'],
			['X','X','-'],
		]))
	
		self.assertEqual(1, count_corners([
			['X','X','X'],
			['X','X','='],
			['X','+','-'],
		]))
	
		self.assertEqual(1, count_corners([
			['X','X','X'],
			['X','X','X'],
			['-','X','X'],
		]))
	
		self.assertEqual(1, count_corners([
			['X','X','X'],
			['=','X','X'],
			['-','+','X'],
		]))

		self.assertEqual(4, count_corners([
			['X','-','X'],
			['-','X','-'],
			['X','-','X'],
		]))

		self.assertEqual(4, count_corners([
			['-','-','-'],
			['-','X','-'],
			['-','-','-'],
		]))
	
		self.assertEqual(4, count_corners([
			['-','1','-'],
			['4','X','2'],
			['-','3','-'],
		]))
	
		self.assertEqual(4, count_corners([
			['1','-','2'],
			['-','X','-'],
			['3','-','4'],
		]))

if __name__ == '__main__':
    unittest.main()
