import sys
import pprint
import time
import functools

def get_part():
	if len(sys.argv) > 1:
			return 2 if sys.argv[1] == '2' else 1
	
	return 1

def load_input(input_file: str) -> list[str]:
	f = open(input_file, "r")

	codes = []
	for pattern in f.readlines():
		codes.append(pattern.strip())

	return (codes)

# numeric keypad - 1
# 	+---+---+---+
#   | 7 | 8 | 9 |
#   +---+---+---+
#   | 4 | 5 | 6 |
#   +---+---+---+
#   | 1 | 2 | 3 |
#   +---+---+---+
#       | 0 | A |
#       +---+---+

NUMERIC = [
	['7', '8', '9'],
	['4', '5', '6'],
	['1', '2', '3'],
	['#', '0', 'A'],
]

# directional keypad - 2 & 3
#    	  +---+---+
#				| ^ | A |
#		+---+---+---+
#		| < | v | > |
#		+---+---+---+
#

DIRECTIONAL = [
	['#', '^', 'A'],
	['<', 'v', '>'],
]

def get_neighbors(i,j,grid):
	neighbors = []

	for di, dj, ins in [(-1,0, '^'), (0,1, '>'), (1,0, 'v'), (0,-1, '<')]:
		i2 = i + di
		j2 = j + dj

		if i2 < 0 or i2 >= len(grid) or j2 < 0 or j2 >= len(grid[0]) or grid[i2][j2] == '#':
			continue

		neighbors.append((grid[i2][j2], ins))

	return neighbors
		

def build_nodes(grid):
	nodes = {}

	for i in range(len(grid)):
		for j in range(len(grid[i])):
			if grid[i][j] == '#':
				continue

			nodes[grid[i][j]] = get_neighbors(i,j,grid)

	return nodes


def count_turns(path):
	t = 0

	for i in range(len(path)):
		if i != 0 and path[i] != path[i-1]:
			t += 1

	return t

def pick_best(pathA, pathB):
	# turns are expensive downstream
	ta = count_turns(pathA)
	tb = count_turns(pathB)

	if ta != tb:
		return pathA if ta < tb else pathB
	

	# if all else is the same, chose the shortest path
	#print("same turns", pathA, pathB)
	return pathA if len(pathA) < len(pathB) else pathB

def solve_nodes(nodes):
	solves = {}
	for n in nodes:
		solves[n] = {}
		solves[n][n] = ''

		queue = list(map(lambda x: (x[0], x[1]) , nodes[n]))
		visited = set([n])
		
		while len(queue) > 0:
			key, instructions = queue.pop(0)
			visited.add(key)

			if key not in solves[n]:
				solves[n][key] = instructions
			else:
				solves[n][key] = pick_best(solves[n][key], instructions) 

			for neighbor in nodes[key]:
				if neighbor[0] not in visited:
					queue.append((neighbor[0], instructions + neighbor[1]))

		for key in solves[n]:
			solves[n][key] += 'A'

				
	return solves

def parse_numeric_code(code) -> int:
	return int("".join(filter(lambda x: x.isdigit(), code)))

numeric_nodes = build_nodes(NUMERIC)
numeric_solve = solve_nodes(numeric_nodes)
directional_nodes = build_nodes(DIRECTIONAL)
directional_solve = solve_nodes(directional_nodes)


@functools.cache
def solve(code, depth):
	if depth == 0:
		return len(code)
	
	result = 0
	prev = "A"
	for cur in code:
		solution = directional_solve if prev in directional_solve and cur in directional_solve else numeric_solve
		result += solve(solution[prev][cur], depth-1)
		prev = cur

	return result

def main():
	t1 = time.time()
	codes = load_input('input.txt')


	sum_complexity = 0
	depth = 3 if get_part() == 1 else 26

	print(f'running part {get_part()}')
	print(f'handling {depth} solves')
	for code in codes:	
		numeric_part = parse_numeric_code(code)
		shortest_seq = solve(code, depth)
	
		print(code, numeric_part, shortest_seq)

		sum_complexity += (numeric_part * shortest_seq)

	print('total complexity', sum_complexity)


	print(f"part {get_part()}: took {round(time.time()-t1, 5)}s")
if __name__=='__main__':
	main()
