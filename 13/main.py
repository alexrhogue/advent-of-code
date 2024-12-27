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


""" def solve_machine(aX, aY, bX, bY, curX, curY, targetX, targetY):
	print(aX, aY, bX, bY, curX, curY, targetX, targetY)

	if curX == targetX and curY == targetY:
		return 0
	
	if curX > targetX or curY > targetY:
		return -1
	
	a = solve_machine(aX, aY, bX, bY, curX + aX, curY + aY, targetX, targetY)
	b = solve_machine(aX, aY, bX, bY, curX + bX, curY + bY, targetX, targetY)

	if a == -1 and b == -1:
		return -1
	
	if a == -1:
		return b + 3
	
	if b == -1:
		return a + 1
	
	a += 1
	b += 3

	return a if a < b else b """

def solve_machine(aX, aY, bX, bY, targetX, targetY):
	numA = round(min(targetX / aX, targetY / aY))
	numB = 0
	cost = -1

	while(numA >= 0):
		curX = numA * aX + numB * bX 
		curY = numA * aY + numB * bY

		if numA == 80:
			print(numA,numB)
			print(curX,curY)

		if curX == targetX and curY == targetY:
			new_cost = (3 * numA) + numB
			print(new_cost)
			if numA <= 100 and numB <= 100 and (cost == -1 or new_cost < cost):
				cost = new_cost

		if curX < targetX or curY < targetY:
			numB += 1
		else:
			numA -= 1

	return cost



def main():
	machines = load_input("input.txt")

	cost_to_win = 0
	for machine in machines:
		a, b, target = machine
		cost = solve_machine(a[0], a[1], b[0], b[1], target[0], target[1])

		if cost > -1:
			cost_to_win += cost


	print('cost to win', cost_to_win)
    
if __name__=="__main__":
	main()
