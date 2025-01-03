import sys
import heapq
import time

def get_part():
	if len(sys.argv) > 1:
			return 2 if sys.argv[1] == '2' else 1
	
	return 1

def load_input(input_file: str) -> list[str]:
	f = open(input_file, "r")

	grid = []
	for line in f.readlines():
		grid.append(list(line.strip()))

	return grid

def pretty_print(grid):
	print('---')
	for i in range(len(grid)):
		print("".join(grid[i]))
	print('---')

def get_loc(c, grid):
	for i in range(len(grid)):
		for j in range(len(grid[i])):
			if grid[i][j] == c:
				return (i,j)

def solve_grid(grid, si, sj, ei, ej):
	grid_size = len(grid)
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

			if i2 < 0 or i2 >= grid_size or j2 < 0 or j2 >= grid_size or grid[i2][j2] == '#':
				continue
			
			d2 = d + 1
			if (i2,j2) not in dist or dist[(i2,j2)] > d2:
				dist[(i2,j2)] = d2
				heapq.heappush(q, (d2, i2, j2))

	return dist


def main():
	t1 = time.time()
	grid = load_input('input.txt')
	pretty_print(grid)
	si, sj = get_loc('S', grid)
	ei, ej = get_loc('E', grid)

	if get_part() == 1:
		pretty_print(grid)
		dist = solve_grid(grid, si, sj, ei, ej)
		print('shortest path',  dist[(ei, ej)] if (ei, ej) in dist else -1)
	else:
		print('TODO')



	t2 = time.time()

	print(f'part {get_part()}: took {round(t2-t1, 5)}s')
if __name__=='__main__':
	main()
