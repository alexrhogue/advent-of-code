import re
import math
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_pdf import PdfPages
from collections import Counter

digit_regex = re.compile(r'-?\d+')

def load_input(input_file: str) -> list[str]:
	f = open(input_file, "r")

	reading_map = True

	warehouse = []
	moves = []
	for line in f.readlines():
		if len(line.strip()) == 0:
			reading_map = False
		elif reading_map:
			warehouse.append(list(line.strip()))
		else:	
			moves += list(line.strip())


	return warehouse, moves

def pretty_print(warehouse):
	for i in range(len(warehouse)):
		print(warehouse[i])

def get_start(warehouse):
	for i in range(len(warehouse)):
		for j in range(len(warehouse)):
			if warehouse[i][j] == '@':
				return (i,j)

MOVES = {
	"^": (-1, 0),
	">": (0, 1),
	"v": (1, 0),
	"<": (0, -1),
}

EMPTY = "."
WALL = "#"
BOX = "O"

def swap(i, j, i2, j2, warehouse):
	tmp = warehouse[i2][j2]
	warehouse[i2][j2] = warehouse[i][j]
	warehouse[i][j] = tmp

def move(i,j, move_cmd, warehouse):
	mI, mJ = MOVES[move_cmd]
	i2 = i + mI
	j2 = j + mJ

	if warehouse[i2][j2] == WALL:
		return (i,j)

	if warehouse[i2][j2] == EMPTY:
		swap(i, j, i2, j2, warehouse)
		return (i2, j2)

	

	while(warehouse[i2][j2] != WALL and warehouse[i2][j2] != EMPTY):
		i2 += mI
		j2 += mJ

	# print(i,j, move_cmd, mI, mJ, i2, j2)
	if warehouse[i2][j2] == WALL:
		# print('dont move')
		return (i,j)


	moved = False
	while i != i2 or j != j2:
		# print(i2,j2,i2 - mI,j2 - mJ)
		moved = True
		swap(i2, j2, i2 - mI, j2 - mJ, warehouse)
		i2 -= mI
		j2 -= mJ


	return (i,j) if not moved else (i + mI, j + mJ)

def calc_gps(warehouse):
	gps = 0
	for i in range(len(warehouse)):
		for j in range(len(warehouse)):
			if warehouse[i][j] == BOX:
				gps += i * 100 + j
			
	return gps


def main():
	warehouse, move_cmds = load_input("input.txt")

	i, j = get_start(warehouse)

	for move_cmd in move_cmds:
		i,j = move(i, j, move_cmd, warehouse)
		#pretty_print(warehouse)

	print('gps', calc_gps(warehouse))

    
if __name__=="__main__":
	main()
