import sys
import pprint
import time

def get_part():
	if len(sys.argv) > 1:
			return 2 if sys.argv[1] == '2' else 1
	
	return 1

def load_input(input_file: str) -> list[str]:
	f = open(input_file, "r")

	codes = []
	for pattern in f.readlines():
		codes.append(list(pattern.strip()))

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


def solve_nodes(nodes):
	solves = {}
	for n in nodes:
		solves[n] = {}
		solves[n][n] = [[]]

		queue = list(map(lambda x: (x[0], [x[1]]) , nodes[n]))
		visited = set([n])
		
		while len(queue) > 0:
			key, instructions = queue.pop(0)
			visited.add(key)

			if key not in solves[n]:
				solves[n][key] = [instructions]
			else:
				solves[n][key].append(instructions)

			for neighbor in nodes[key]:
				if neighbor[0] not in visited:
					queue.append((neighbor[0], instructions + [neighbor[1]]))

				
	return solves

def parse_numeric_code(code) -> int:
	return int("".join(filter(lambda x: x.isdigit(), code)))

def solve_code(code, solve):
	solutions = []
	
	prev = 'A'
	for key in code:
		solutions.append(list(map(lambda x: x + ['A'], solve[prev][key])))
		prev = key

	options = []
	for i in range(len(solutions)):
		new_options = []
		for j in range(len(solutions[i])):
			if i == 0:
				new_options.append(solutions[i][j])
			else:
				for k in range(len(options)):
					new_options.append(options[k] + solutions[i][j])


		options = new_options

	return options

def solve(start_code, solves):
	codes = [start_code]
	for solve in solves:
		new_codes = []
		for code in codes:
			new_codes += solve_code(code, solve)

		codes = new_codes


	return sorted(codes, key = lambda x: len(x))[0]

def main():
	t1 = time.time()
	codes = load_input('input.txt')

	numeric_nodes = build_nodes(NUMERIC)
	numeric_solve = solve_nodes(numeric_nodes)
	directional_nodes = build_nodes(DIRECTIONAL)
	directional_solve = solve_nodes(directional_nodes)

	sum_complexity = 0
	solves = [numeric_solve]
	for i in range(0, 2 if get_part() == 1 else 25):
		solves.append(directional_solve)

	print(f'running part {get_part()}')
	print(f'handling {len(solves)} solves')
	for code in codes:	
		numeric_part = parse_numeric_code(code)
		shortest_seq = solve(code, solves)
	
		print(code, numeric_part, len(shortest_seq))

		sum_complexity += (numeric_part * len(shortest_seq)) 

	print('total complexity', sum_complexity)


	print(f"part {get_part()}: took {round(time.time()-t1, 5)}s")
if __name__=='__main__':
	main()
