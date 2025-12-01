import re
import numpy as np

digit_regex = re.compile(r'-?\d+')

def scale_input(input):
	if input == '#':
		return ['#','#']
	if input == 'O':
		return ['[',']']
	if input == '.':
		return ['.','.']
	if input == '@':
		return ['@', '.']
	
def load_input(input_file: str) -> list[str]:
	f = open(input_file, "r")

	reading_map = True

	warehouse = []
	moves = []
	for line in f.readlines():
		if len(line.strip()) == 0:
			reading_map = False
		elif reading_map:
			warehouse.append(np.concat(list(map(scale_input, line.strip()))))
		else:	
			moves += list(line.strip())


	return warehouse, moves

def pretty_print(warehouse):
	for i in range(len(warehouse)):
		print("".join(warehouse[i]))
	print('---')

def get_start(warehouse):
	for i in range(len(warehouse)):
		for j in range(len(warehouse[i])):
			if warehouse[i][j] == '@':
				return (i,j)

MOVES = {
	'^': (-1, 0),
	'>': (0, 1),
	'v': (1, 0),
	'<': (0, -1),
}

EMPTY = '.'
WALL = '#'
BOX = ['[', ']']

def swap(i, j, i2, j2, warehouse):
	tmp = warehouse[i2][j2]
	warehouse[i2][j2] = warehouse[i][j]
	warehouse[i][j] = tmp

def get_box_coords(i,j,warehouse):
	if warehouse[i][j] == '[':
		return [(i,j), (i, j+1)]
	
	if warehouse[i][j] == ']':
		return [(i,j-1), (i, j)]
	
	return None

def push_box_h(i,j, mi, mj, warehouse):
	i2 = i
	j2 = j

	while(warehouse[i2][j2] != WALL and warehouse[i2][j2] != EMPTY):
		i2 += mi
		j2 += mj

	if warehouse[i2][j2] == WALL:
		return (i,j)

	while i != i2 or j != j2:
		swap(i2, j2, i2 - mi, j2 - mj, warehouse)
		i2 -= mi
		j2 -= mj

def push_box_v(i,j, mi, mj, warehouse):
	left, right = get_box_coords(i,j,warehouse)

	leftObj = warehouse[left[0] + mi][left[1]]
	rightObj = warehouse[right[0] + mi][right[1]]

	if leftObj == WALL or rightObj == WALL:
		return []
	
	leftMove = [left] if leftObj == EMPTY else []
	rightMove = [right] if rightObj == EMPTY else []

	if len(leftMove) == 0:
		leftMove = push_box_v(left[0] + mi, left[1], mi, mj, warehouse)
		if len(leftMove) > 0:
			leftMove = [left] + leftMove

	if len(rightMove) == 0:
		rightMove = push_box_v(right[0] + mi, right[1], mi, mj, warehouse)
		if len(rightMove) > 0:
			rightMove = [right] + rightMove

	if len(leftMove) > 0 and len(rightMove) > 0:
		return  leftMove + rightMove
	
	return []
	

def move(i,j, move_cmd, warehouse):
	mi, mj = MOVES[move_cmd]
	i2 = i + mi
	j2 = j + mj

	if warehouse[i2][j2] == WALL:
		return (i,j)
	
	if warehouse[i2][j2] in BOX:
		if move_cmd == '<' or move_cmd == ">":
			push_box_h(i2,j2,mi,mj,warehouse)
		else:
			moves = push_box_v(i2,j2,mi,mj,warehouse)
			moves = sorted(list(set(moves)), key = lambda m: m[0], reverse=True if mi > 0 else False)
			for move in moves:
				swap(move[0], move[1], move[0] + mi, move[1] + mj, warehouse)


	if warehouse[i2][j2] == EMPTY:
		swap(i, j, i2, j2, warehouse)
		return (i2, j2)

	return (i, j)

def calc_gps(warehouse):
	gps = 0
	for i in range(len(warehouse)):
		for j in range(len(warehouse[i])):
			if warehouse[i][j] in ['O', '[']:
				gps += i * 100 + j
			
	return gps

def main():
	warehouse, move_cmds = load_input('input.txt')
	pretty_print(warehouse)
	i, j = get_start(warehouse)

	for move_cmd in move_cmds:
		# print(move_cmd)
		i,j = move(i, j, move_cmd, warehouse)

	pretty_print(warehouse)
	print('gps', calc_gps(warehouse))

    
if __name__=='__main__':
	main()
