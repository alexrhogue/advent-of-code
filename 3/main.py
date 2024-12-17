from collections import namedtuple
import re

def load_input(input_file: str) -> list[str]:
	f = open(input_file, "r")
	lines = f.readlines()

	return lines
      
OP_MULTIPLY = 'mul'
OP_DO = 'do'
OP_DONT = 'don\'t'

Command = namedtuple('Command', ['op', 'params'])

cmd_regex = re.compile(r"don't\(\)|do\(\)|mul\(\d{1,3},\d{1,3}\)")
digit_regex = re.compile(r'\d{1,3}')

def parse_mem(mem: str) -> list[Command]:
	matches = cmd_regex.findall(mem)

	commands = []
	for str_cmd in matches:
		if str.startswith(str_cmd, OP_DONT):
			commands.append(Command(OP_DONT, []))
		elif str.startswith(str_cmd, OP_DO):
			commands.append(Command(OP_DO, []))
		else:
			digits = digit_regex.findall(str_cmd)
			commands.append(Command(OP_MULTIPLY, [int(x) for x in digits]))

	return commands

def execute_arithmetic_command(command: Command) -> int:
	if command.op == OP_MULTIPLY:
		result = 1
		for param in command.params:
			result *= param

		return result
	
	return 0

def execute_control_command(cmd: Command) -> bool:
	if cmd.op == OP_DO:
		return True
	
	if cmd.op == OP_DONT:
		return False
	
	print("unknown control cmd", cmd.op)

def execute_commands(commands: list[Command]) -> int:
	sum = 0
	do = True

	for cmd in commands:
		if cmd.op == OP_DO or cmd.op == OP_DONT:
			do = execute_control_command(cmd)
		elif cmd.op == OP_MULTIPLY:
			if do:
				sum += execute_arithmetic_command(cmd)
		else:
			print("unknown cmd", cmd.op)

	return sum


def main():
	mem_lines = load_input("input.txt")

	commands = []
	for mem in mem_lines:
		commands = commands + parse_mem(mem)

	sum = execute_commands(commands)
	
	print("sum", sum)
    
if __name__=="__main__":
	main()
