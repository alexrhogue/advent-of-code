import re

digit_regex = re.compile(r'\d+')

def load_input(input_file: str) -> list[str]:
	f = open(input_file, "r")

	lines = [[]]
	for line in f.readlines():
		if len(line.strip()) == 0:
			lines.append([])
		else:
			lines[len(lines) - 1].append([int(x) for x in digit_regex.findall(line)])

	return lines

def solve_machine(aX, aY, bX, bY, targetX, targetY):
	numA = (targetX * bY - bX * targetY) / (aX * bY - bX * aY)
	numB = (aX * targetY - targetX * aY) / (aX * bY - bX * aY)

	if numA.is_integer() and numB.is_integer():
		return 3 * int(numA) + int(numB)
	
	return 0



def main():
	machines = load_input("input.txt")

	pt_2 = True
	cost_to_win = 0
	for machine in machines:
		a, b, target = machine
		if pt_2:
			target[0] += 10000000000000
			target[1] += 10000000000000
		cost = solve_machine(a[0], a[1], b[0], b[1], target[0], target[1])

		if cost > -1:
			cost_to_win += cost


	print('cost to win', cost_to_win)
    
if __name__=="__main__":
	main()
