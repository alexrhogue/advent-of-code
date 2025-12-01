from main import execute_arithmetic_command, parse_mem, Command, OP_MULTIPLY, OP_DO, OP_DONT, execute_control_command, execute_commands

import unittest

class Test(unittest.TestCase): 
	
	def test_parse_meme(self): 
		self.assertEqual([], parse_mem(""))
		self.assertEqual([], parse_mem("23fahd7f723489"))
		self.assertEqual([], parse_mem("mul(a,1)"))
		self.assertEqual([], parse_mem("mul(1,3!"))
		self.assertEqual([], parse_mem("mul[1,3]"))
		self.assertEqual([], parse_mem("mul(1 ,4 )"))

		self.assertEqual([Command(OP_MULTIPLY, [2,3])], parse_mem("mul(2,3)"))
		self.assertEqual([Command(OP_MULTIPLY, [1,323])], parse_mem("mul(1,323)"))
		self.assertEqual([Command(OP_MULTIPLY, [231,30])], parse_mem("mul(231,30)"))
		self.assertEqual([Command(OP_MULTIPLY, [2,1])], parse_mem("dont_mul(2,1)"))
		self.assertEqual([Command(OP_DONT, []), Command(OP_MULTIPLY, [2,1])], parse_mem("don\'t()mul(2,1)"))



	def test_execute_arithmetic_command(self): 
		self.assertEqual(10, execute_arithmetic_command(Command(OP_MULTIPLY, [2,5])))
		self.assertEqual(0, execute_arithmetic_command(Command(OP_MULTIPLY, [0,1])))
		self.assertEqual(100, execute_arithmetic_command(Command(OP_MULTIPLY, [2,5,10])))
		self.assertEqual(0, execute_arithmetic_command(Command(OP_MULTIPLY, [2,0,10])))

		
	def test_execute_arithmetic_command(self): 
		self.assertEqual(True, execute_control_command(Command(OP_DO, [])))
		self.assertEqual(False, execute_control_command(Command(OP_DONT, [])))

		
	def test_execute_commands(self): 
		self.assertEqual(10, execute_commands([
			Command(OP_DO, []),
			Command(OP_MULTIPLY, [2,5])
		]))

		self.assertEqual(0, execute_commands([
			Command(OP_DONT, []),
			Command(OP_MULTIPLY, [2,5])
		]))

		self.assertEqual(9, execute_commands([
			Command(OP_DONT, []),
			Command(OP_MULTIPLY, [2,5]),
			Command(OP_DO, []),
			Command(OP_MULTIPLY, [3,3])
		]))


if __name__ == '__main__':
    unittest.main()
