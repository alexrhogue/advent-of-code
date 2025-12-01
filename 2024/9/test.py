from main import reformat_disk_v2

import unittest

class Test(unittest.TestCase): 

	def test_reformat_disk_v2(self): 
		self.assertEqual([0,'.'], reformat_disk_v2(['.', 0]))
		self.assertEqual([0,0,2,2,1,'.','.','.','.'], reformat_disk_v2([0,0,'.','.',1,'.',2,2,'.']))
		self.assertEqual([0,0,1,'.',2,2,'.','.','.',], reformat_disk_v2([0,0,'.',1,'.','.',2,2,'.']))
		self.assertEqual([0,0,3,1,'.','.',2,2,'.'], reformat_disk_v2([0,0,'.',1,'.',3,2,2,'.']))
		self.assertEqual([0,6,1,5,2,4,3,'.','.','.','.','.','.',], reformat_disk_v2([0,'.',1,'.',2,'.',3,'.',4,'.',5,'.',6]))

		

if __name__ == '__main__':
    unittest.main()
