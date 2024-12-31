
import re
import sys

digit_regex = re.compile(r'-?\d+')

def load_input(input_file: str) -> list[str]:
	f = open(input_file, "r")

	registers = []
	program = []

	for line in f.readlines():
		digits = [int(x) for x in digit_regex.findall(line)]

		if len(digits) == 1:
			registers.append(digits[0])
		else:
			program += digits

	return (program, registers)

DEFAULT_STEP = 2
	
def combo(operand, registers):
	if operand >= 0 and operand <= 3:
		return operand
	
	return registers[operand % 4]

def op(opcode, operand, output, registers):
	# 0 - adv
	if opcode == 0:
		numerator = registers[0]
		denominator = pow(2, combo(operand, registers))
		registers[0] = int(numerator/denominator)
	
	# 1 - bxl
	elif opcode == 1:
		registers[1] = registers[1] ^ operand
	
	# 2 - bst
	elif opcode == 2:
		registers[1] = combo(operand, registers) % 8
	
	# 3 - jnz
	elif opcode == 3:
		if registers[0] != 0:
			return operand
	
	# 4 - bxc
	elif opcode == 4:
		registers[1] = registers[1] ^ registers[2]
		
	# 5 - out
	elif opcode == 5:
		output.append(combo(operand, registers) % 8)
	
	# 6 - bdv
	elif opcode == 6:
		numerator = registers[0]
		denominator = pow(2, combo(operand, registers))
		registers[1] = int(numerator/denominator)
	
	# 7 - cdv
	elif opcode == 7:
		numerator = registers[0]
		denominator = pow(2, combo(operand, registers))
		registers[2] = int(numerator/denominator)
	

""" 
original start: 35184372088832
stopped at: 35185100681149

"""

def run_program(program, registers):
	output = []

	pointer = 0
	output = []
	#print(registers, list(map(oct,registers)), output, list(map(oct,output)))
	while pointer < len(program) - 1:
		#print(program[pointer], program[pointer + 1])
		newPointer = op(program[pointer], program[pointer + 1], output, registers)
		if newPointer is None:
			pointer += DEFAULT_STEP
		else:
			pointer = newPointer
		
		#print(registers, list(map(bin,registers)), list(map(oct,registers)), output, list(map(oct,output)))
			
	return output

# starts from the last output
# what's the smallest numbers that makes zero?
 # shift it left 3 bits - what's the smallest number (000-111) that makes 3 and so on
def solve_program(program):
	output = []

	input = 0
	target_index = len(program) - 1

	while target_index >= 0:
		for i in range(7):
			# print(input)
			input += 1
			output = run_program(program, [input, 0, 0])

			if output[0] == program[target_index]:
				break
			
		if output == program[target_index:len(program)]:
			print('match', input, bin(input),  program[target_index], output)
			target_index -= 1
			input = input << 3
		else:
			print('going back')
			target_index += 1
			input = input >> 3
		

def get_part():
	if len(sys.argv) > 1:
			return 2 if sys.argv[1] == '2' else 1
	
	return 1


def main():
	part = get_part()
	(program, registers) = load_input('input.txt')

	
	print(program)
	print(registers)

	print("running part", part)
	if part == 1:
		output = run_program(program, registers)
		print('output:', ','.join(map(lambda x: str(x), output)))
	else:
		solve_program(program)
	

if __name__=='__main__':
	main()

	"""
	
def solve_program(program, registers):
	curA = registers[0]
	output = []

	print('starting at', curA)
	while True:
		pointer = 0
		output = []
		registers = [curA,0,0]
		while pointer < len(program) - 1:
			newPointer = op(program[pointer], program[pointer + 1], output, registers)
			if newPointer is None:
				pointer += DEFAULT_STEP
			else:
				pointer = newPointer

			if len(output) > 0 and output != program[0:len(output)]:
				break

		if len(output) > 6:
			print(curA, 'near hit', output)

		if output == program:
			break
		
		curA += 1

	print("lowest a", curA)
	return output
	"""
