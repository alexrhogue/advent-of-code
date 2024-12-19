from main import eval, concat_math

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

if __name__ == '__main__':
    unittest.main()
