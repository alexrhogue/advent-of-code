import sys
import heapq

def get_part():
	if len(sys.argv) > 1:
			return 2 if sys.argv[1] == '2' else 1
	
	return 1

def load_input(input_file: str) -> list[str]:
	f = open(input_file, "r")

	falling_bytes = []

	for line in f.readlines():
		falling_bytes.append([int(x) for x in line.split(',')])

	return falling_bytes

def pretty_print(grid):
	print('---')
	for i in range(len(grid)):
		print("".join(grid[i]))
	print('---')

def sim_falling(falling_byes, start, stop, grid):
	for i in range(start,stop):
		byte_loc = falling_byes[i]
		grid[byte_loc[1]][byte_loc[0]] = "#"

def solve_grid(grid, si, sj, ei, ej):
	dist = {}
	q = []

	heapq.heappush(q, (0, si, sj))
	dist[(si,sj)] = 0

	while q:
		d,i,j = heapq.heappop(q)

		if dist[(i,j)] < d:
			continue

		for dir in [(-1,0),(0,1),(1,0),(0,-1)]:
			i2 = i + dir[0]
			j2 = j + dir[1]

			if i2 < 0 or i2 >= GRID_SIZE or j2 < 0 or j2 >= GRID_SIZE or grid[i2][j2] == '#':
				continue
			
			d2 = d + 1
			if (i2,j2) not in dist or dist[(i2,j2)] > d2:
				dist[(i2,j2)] = d2
				heapq.heappush(q, (d2, i2, j2))

	return dist

GRID_SIZE = 71
def main():
	falling_bytes = load_input('input.txt')

	if get_part() == 1:
		grid = [ ['.']*GRID_SIZE for i in range(GRID_SIZE)]
		sim_falling(falling_bytes, 0, 1024, grid)
		pretty_print(grid)
		dist = solve_grid(grid, 0, 0, 70,70)
		print("shortest path",  dist[(70,70)] if (70,70) in dist else -1)

	else:
		print("todo")
	

if __name__=='__main__':
	main()
