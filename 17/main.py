
import re

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
	
def run_program(program, registers):
	pointer = 0
	output = []
	while pointer < len(program) - 1:
		newPointer = op(program[pointer], program[pointer + 1], output, registers)
		if newPointer is None:
			pointer += DEFAULT_STEP
		else:
			pointer = newPointer

	return output

def main():
	(program, registers) = load_input('input.txt')
	
	print(program, registers)
	output = run_program(program, registers)
	print(','.join(map(lambda x: str(x), output)))

if __name__=='__main__':
	main()