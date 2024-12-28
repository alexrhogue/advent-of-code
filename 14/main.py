import re
import math

digit_regex = re.compile(r'-?\d+')

def load_input(input_file: str) -> list[str]:
	f = open(input_file, "r")

	lines = []
	for line in f.readlines():
		lines.append([int(x) for x in digit_regex.findall(line)])

	return lines


def move(px, py, vx, vy, width, height, moves):
	x = (px + (vx * moves)) % width
	y = (py + (vy * moves)) % height

	return (x,y)

def calc_safety_factor(positions, width, height):
	scores = [0,0,0,0]

	midX = int(width/2)
	midY = int(height/2)
	for x,y in positions:
		if x < midX and y < midY:
			scores[0] += 1
		elif x > midX and y < midY:
			scores[1] += 1
		elif x < midX and y > midY:
			scores[2] += 1
		elif x > midX and y > midY:
			scores[3] += 1



	return math.prod(scores)

def main():
	robots = load_input("input.txt")

	width = 101
	height = 103
	moves = 100

	positions = []
	for robot in robots:
		px, py, vx, vy = robot
		positions.append(move(px, py, vx, vy, width, height, moves))


	print(positions)
	print('safety factor', calc_safety_factor(positions, width, height))
    
if __name__=="__main__":
	main()
