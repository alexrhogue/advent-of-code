from main import get_rotation_cost

import unittest

class Test(unittest.TestCase): 

  def test_get_rotation_cost(self):
    self.assertEqual(0, get_rotation_cost(0,0))
    self.assertEqual(1000, get_rotation_cost(0,1))
    self.assertEqual(2000, get_rotation_cost(0,2))
    self.assertEqual(1000, get_rotation_cost(0,3))

    self.assertEqual(1000, get_rotation_cost(1,0))
    self.assertEqual(0, get_rotation_cost(1,1))
    self.assertEqual(1000, get_rotation_cost(1,2))
    self.assertEqual(2000, get_rotation_cost(1,3))

    self.assertEqual(2000, get_rotation_cost(2,0))
    self.assertEqual(1000, get_rotation_cost(2,1))
    self.assertEqual(0, get_rotation_cost(2,2))
    self.assertEqual(1000, get_rotation_cost(2,3))

    self.assertEqual(1000, get_rotation_cost(3,0))
    self.assertEqual(2000, get_rotation_cost(3,1))
    self.assertEqual(1000, get_rotation_cost(3,2))
    self.assertEqual(0, get_rotation_cost(3,3))
    
if __name__ == '__main__':
    unittest.main()
