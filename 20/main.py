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

def pretty_print_time_saved(time_saved, min_time_save):
	count = {}
	times = set()
	for t in time_saved:
			if t < min_time_save:
				continue

			times.add(t)
			if t in count:
				count[t] += 1
			else:
				count[t] = 1

	for t in sorted(times):
		print(f'- There are {count[t]} cheats that saved {t} picoseconds.')

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

def calc_time_saved_with_cheat(ei, ej, max_cheat_length, dist, path, grid):
	time_saved = []
	for (i,j) in path:
		if i == ei and j == ej:
			continue
		
		for (i2,j2, cheat_dist) in get_reachable_cells(i, j, max_cheat_length, dist):
			if cheat_dist < dist[(i2,j2)]:
				time_saved.append(dist[(i2,j2)] - cheat_dist)

	return time_saved

def main():
	t1 = time.time()
	grid = load_input('input.txt')
	si, sj = get_loc('S', grid)
	ei, ej = get_loc('E', grid)

	dist, path = solve_grid(grid, si, sj, ei, ej)
	cheat_size = 1
	min_time_save = 100
	if get_part() != 1:
		cheat_size = 20

	time_saved = calc_time_saved_with_cheat(ei, ej, cheat_size, dist, path, grid)

	pretty_print_time_saved(time_saved, min_time_save)
	print('shortest path',  dist[(ei, ej)] if (ei, ej) in dist else -1)
	print(f'# cheats that saved >= {min_time_save} picoseconds', len(list(filter(lambda c: c >= min_time_save, time_saved))))

	t2 = time.time()
	print(f'part {get_part()}: took {round(t2-t1, 5)}s')
if __name__=='__main__':
	main()

# correct answers = 1448 1017615
