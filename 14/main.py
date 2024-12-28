import re
import math
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_pdf import PdfPages
from collections import Counter

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

def worth_rendering(x,y):
	rows = Counter(y)
	return rows.most_common(1)[0][1] > 15

def main():
	robots = load_input("input.txt")

	width = 101
	height = 103
	moves = 10000

	with PdfPages('positions.pdf') as pdf:
		for moves in range(moves):
			x = []
			y = []
			for robot in robots:
				px, py, vx, vy = robot
				result = move(px, py, vx, vy, width, height, moves)

				x.append(result[0])
				y.append(result[1])

			if worth_rendering(x,y):
				plt.figure()
				plt.gca().invert_yaxis()
				plt.title(f'{moves}')
				plt.scatter(x, y)
				pdf.savefig()
				plt.close()



    
if __name__=="__main__":
	main()
