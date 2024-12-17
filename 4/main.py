from collections import namedtuple

def load_input(input_file: str) -> list[str]:
	f = open(input_file, "r")
	lines = f.readlines()

	return lines
      

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
