from main import eval, concat_math, is_target_possible, unconcat_math

import unittest

class Test(unittest.TestCase): 

	def test_eval(self): 
		self.assertEqual([], eval([]))
		self.assertEqual([1], eval([1]))
		self.assertCountEqual([6, 5, 23], eval([2,3]))
		self.assertCountEqual([9, 10, 20, 24, 234, 92, 27, 54, 64 ], eval([2,3,4]))

	def test_concat_math(self):
		self.assertEqual(12, concat_math(1,2))
		self.assertEqual(102, concat_math(10,2))
		self.assertEqual(120, concat_math(1,20))
		self.assertEqual(2, concat_math(0,2))
		self.assertEqual(666555, concat_math(666,555))
		self.assertEqual(11, concat_math(1,1))
		self.assertEqual(10, concat_math(1,0))

		
		self.assertEqual(1234, concat_math(1,234))
		self.assertEqual(12345, concat_math(12,345))
		self.assertEqual(123456, concat_math(123,456))
		self.assertEqual(12345, concat_math(123,45))
		self.assertEqual(1234, concat_math(123,4))

		
		self.assertEqual(39422310, concat_math(394223, 10))

	def test_unconcat_math(self):
		self.assertEqual(1, unconcat_math(12, 2))
		self.assertEqual(123, unconcat_math(1234, 4))
		self.assertEqual(12, unconcat_math(1234, 34))
		self.assertEqual(1, unconcat_math(1234, 234))


		self.assertEqual(-1, unconcat_math(12, 12))
		self.assertEqual(-1, unconcat_math(224, 2))
		self.assertEqual(-1, unconcat_math(224, 20))
		self.assertEqual(-1, unconcat_math(224, 100))
		self.assertEqual(-1, unconcat_math(224, 1000))

	def test_eval(self): 
		self.assertEqual(True, is_target_possible(1, [1]))
		self.assertEqual(True, is_target_possible(5, [2, 3]))
		self.assertEqual(True, is_target_possible(6, [2, 3]))
		self.assertEqual(False, is_target_possible(1, [2, 3]))
		self.assertEqual(True, is_target_possible(24, [2, 3, 4]))
		self.assertEqual(True, is_target_possible(23, [2, 3]))
		self.assertEqual(True, is_target_possible(234, [2, 3, 4]))
		self.assertEqual(True, is_target_possible(64, [2, 3, 4]))
		self.assertEqual(True, is_target_possible(54, [2, 3, 4])) 

if __name__ == '__main__':
    unittest.main()
