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

def solve(code, passes):
	codes = [code]
	for solve in passes:
		cur_pass = []
		prev = 'A'
		for key in codes[-1]:
			cur_pass = cur_pass + solve[prev][key][0] + ['A']
			prev = key

		codes.append(cur_pass)
		print("".join(codes[-1]), len(codes[-1]))

	return codes[-1]
	
def main():
	t1 = time.time()
	codes = load_input('input.txt')

	if get_part() == 1:
		numeric_nodes = build_nodes(NUMERIC)
		numeric_solve = solve_nodes(numeric_nodes)
		#print('numeric_solve:')
		#pprint.pprint(numeric_solve)
	
		directional_nodes = build_nodes(DIRECTIONAL)
		directional_solve = solve_nodes(directional_nodes)
		print('directional_solve:')
		pprint.pprint(directional_solve)

		print(len(solve(codes[0], [numeric_solve, directional_solve, directional_solve])))
	else:
		print('todo')


	print(f"part {get_part()}: took {round(time.time()-t1, 5)}s")
if __name__=='__main__':
	main()
