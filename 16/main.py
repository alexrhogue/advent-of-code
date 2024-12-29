import queue
import sys
print(sys.getrecursionlimit())
def load_input(input_file: str) -> list[str]:
	f = open(input_file, "r")
	maze = []
	for line in f.readlines():
		maze.append(list(line.strip()))

	return maze

def pretty_print(maze):
	for i in range(len(maze)):
		print("".join(str(maze[i])))
	print('---')

def get_pos(char, maze):
	for i in range(len(maze)):
		for j in range(len(maze[i])):
			if maze[i][j] == char:
				return (i,j)


EMPTY = '.'
WALL = '#'

# figure out a math way to do this
def get_rotation_cost(from_dir, to_dir):
	if from_dir == to_dir:
		return 0
	
	if abs(to_dir - from_dir) == 2:
		return 2000
	
	return 1000

def get_neighbors(start, dir):
	return [
		[(start[0] - 1, start[1]), 0, 1 + get_rotation_cost(dir, 0)],
		[(start[0], start[1] + 1), 1, 1 + get_rotation_cost(dir, 1)],
		[(start[0] + 1, start[1]), 2, 1 + get_rotation_cost(dir, 2)],
		[(start[0], start[1] - 1), 3, 1 + get_rotation_cost(dir, 3)]
	]

def in_bounds(pos, maze):
	if pos[0] > -1 and pos[1] > -1 and pos[0] < len(maze) and  pos[1] < len(maze[0]):
		return maze[pos[0]][pos[1]] != "#"
	
	return False


def get_all_paths(start_pos, end_pos, start_dir, maze):
	paths = []

	best_score = float('inf')
	q = []
	q.append([start_pos, start_dir, 0, [start_pos]])

	while len(q) > 0:
		pos, dir, score, path = q.pop()
		if pos == end_pos and score <= best_score:
			print(pos, score)
			best_score = score
			paths.append([score, path])
			continue

		for next_pos, next_dir, next_score in get_neighbors(pos, dir):
			if in_bounds(next_pos, maze) and next_pos not in path:
				# abandon paths that are already more costly than current best
				if next_score + score <= best_score:
					next_path = path.copy()
					next_path.append(next_pos)
					q.append([next_pos, next_dir, next_score + score, next_path])
		
	return paths


def analyze_best_path(paths):
	if len(paths) == 0:
		return (float('inf'), float('inf'))
	
	lowest_score = sorted(paths, key=lambda p: p[0])[0][0]
	unique_tiles = set({})
	
	for path in paths:
		if path[0] == lowest_score:
			unique_tiles.update( path[1])

	return (lowest_score, len(unique_tiles))
	

def main():
	maze = load_input('input.txt')
	start = get_pos('S', maze)
	end = get_pos('E', maze)


	pretty_print(maze)
	print('start', start)
	print('end', end)
	paths = get_all_paths(start, end, 1, maze)

	score, num_unique_tiles = analyze_best_path(paths)
	print('lowest score', score)
	print('lowest score unique tiles', num_unique_tiles)
    
if __name__=='__main__':
	main()
