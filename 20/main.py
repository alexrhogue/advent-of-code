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
	path = []
	q = []

	heapq.heappush(q, (0, si, sj))
	dist[(si,sj)] = 0

	while q:
		d,i,j = heapq.heappop(q)

		path.append((i, j))

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

	return dist, path

def get_reachable_cells(ci,cj, max_size, dist):
	reachable_cells = []
	for i in range(ci - (max_size + 1), ci + (max_size + 2)):
		offset = ((max_size + 1) - abs(i - ci))
		for j in range(cj - offset, cj + offset + 1):
			if (i,j) in dist:
				reachable_cells.append((i,j, dist[(ci,cj)] + abs(ci-i) + abs(cj-j)))
		
	return reachable_cells

def calc_cheat_dists(ei, ej, max_cheat_length, dist, path):
	cheat_dists = []
	f = 0
	for (i,j) in path:
		print('-')
		print('(i,j)', i,j, dist[(i,j)])
		if i == ei and j == ej:
			continue
		
		for (i2,j2, cheat_dist) in get_reachable_cells(i, j, max_cheat_length, dist):
			# ignore cheats that cost the same or more than the normal path
			if cheat_dist < dist[(i2,j2)]:
				cheat_dists.append(dist[(i2,j2)] - cheat_dist)


	print(cheat_dists)
	return cheat_dists

def main():
	t1 = time.time()
	grid = load_input('input.txt')
	pretty_print(grid)
	si, sj = get_loc('S', grid)
	ei, ej = get_loc('E', grid)

	pretty_print(grid)
	dist, path = solve_grid(grid, si, sj, ei, ej)
	cheat_size = 1
	f = 1
	if get_part() != 1:
		cheat_size = 20

	cheat_dists = calc_cheat_dists(ei, ej, cheat_size, dist, path)
	print('shortest path',  dist[(ei, ej)] if (ei, ej) in dist else -1)
	print(f'cheats that saved >= {f} picoseconds', len(list(filter(lambda c: c >= f, cheat_dists))))
	

	t2 = time.time()

	print(f'part {get_part()}: took {round(t2-t1, 5)}s')
if __name__=='__main__':
	main()
