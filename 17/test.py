from main import op, combo, DEFAULT_STEP, run_program

import unittest

class Test(unittest.TestCase): 

  def test_combo(self):
     registers = [10,20,30]
     self.assertEqual(0, combo(0, registers))
     self.assertEqual(1, combo(1, registers))
     self.assertEqual(2, combo(2, registers))
     self.assertEqual(3, combo(3, registers))
     self.assertEqual(10, combo(4, registers))
     self.assertEqual(20, combo(5, registers))
     self.assertEqual(30, combo(6, registers))

  def test_op(self):
    # 0 - adv
    registers = [13]
    op(0, 2, [], registers)
    self.assertEqual(3, registers[0])
 
    # 1 - bxl
    registers = [0,12]
    op(1, 5, [], registers)
    self.assertEqual(9, registers[1])
  
    # 2 - bst
    registers = [0,12]
    op(2, 5, [], registers)
    self.assertEqual(4, registers[1])  
	
	  # 3 - jnz
    registers = [0]
    op(3, 5, [], registers)
    self.assertIsNone(self.assertEqual([0], registers))

    registers = [2]
    self.assertEqual(5, op(3, 5, [], registers))

    # 4 - bxc
    registers = [0,12,5]
    op(4, 5, [], registers)
    self.assertEqual(9, registers[1])  
    self.assertEqual(5, registers[2])  
		
	  # 5 - out
    registers = [0,12]
    output = []
    op(5, 5, output, registers)
    self.assertEqual(4, output[0])  

    op(5, 2, output, registers)
    self.assertEqual(2, output[1])  

    # 6 - bdv
    registers = [13,0,0]
    op(6, 2, [], registers)
    self.assertEqual(13, registers[0])
    self.assertEqual(3, registers[1])
    
    # 7 - cdv
    registers = [13,0,0]
    op(7, 2, [], registers)
    self.assertEqual(13, registers[0])
    self.assertEqual(3, registers[2])

  def test_run_program(self):
    registers = [0,0,9]
    self.assertEqual([], run_program([2,6], registers))
    self.assertEqual([0,1,9], registers)

    registers = [10,0,0]
    self.assertEqual([0,1,2], run_program([5,0,5,1,5,4], registers))
    self.assertEqual([10,0,0], registers)

    registers = [2024,0,0]
    self.assertEqual([4,2,5,6,7,7,7,7,3,1,0], run_program([0,1,5,4,3,0], registers))
    self.assertEqual([0,0,0], registers)

    registers = [0,29,0]
    self.assertEqual([], run_program([1,7], registers))
    self.assertEqual([0,26,0], registers)

    registers = [0,2024,43690]
    self.assertEqual([], run_program([4,0], registers))
    self.assertEqual([0,44354,43690], registers)
    
if __name__ == '__main__':
    unittest.main()
