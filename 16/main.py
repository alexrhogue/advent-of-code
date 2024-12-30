import heapq

def load_input(input_file: str) -> list[str]:
	f = open(input_file, "r")
	maze = []
	for line in f.readlines():
		maze.append(list(line.strip()))

	return maze

def pretty_print(maze):
	print('---')
	for i in range(len(maze)):
		print("".join(str(maze[i])))
	print('---')

def get_pos(char, maze):
	for i in range(len(maze)):
		for j in range(len(maze[i])):
			if maze[i][j] == char:
				return (i,j)

# figure out a math way to do this
def get_rotation_cost(from_dir, to_dir):
	if from_dir == to_dir:
		return 0
	
	if abs(to_dir - from_dir) == 2:
		return 2000
	
	return 1000

def get_next(i, j, dir):
	move = [
		(i - 1, j),
		(i, j + 1),
		(i + 1, j),
		(i, j - 1)
	]

	return move[dir]

def get_rotations(from_dir):
	return map(lambda to_dir: [to_dir, get_rotation_cost(from_dir, to_dir)], filter(lambda to_dir: to_dir != from_dir, [0,1,2,3]))

def in_bounds(i, j, maze):
	if i > -1 and j > -1 and i < len(maze) and j < len(maze[0]):
		return maze[i][j] != "#"
	
	return False

def get_all_paths(start, maze):
	dist = {}
	nodes = []
	
	for (start_i, start_j, start_dir) in start:
		dist[(start_i, start_j, start_dir)] = 0
		heapq.heappush(nodes, [0, start_i, start_j, start_dir])

	while nodes:
		score, i, j, dir = heapq.heappop(nodes)

		if dist[(i,j,dir)] < score:
			continue

		for next_dir, score_increase in get_rotations(dir):
				next_score = score_increase + score

				if (i, j, next_dir) not in dist or next_score < dist[(i, j, next_dir)]:
					dist[(i, j, next_dir)] = next_score
					heapq.heappush(nodes, [next_score, i, j, next_dir])

		(next_i, next_j) = get_next(i, j, dir) 
		next_score = 1 + score

		if in_bounds(next_i, next_j, maze) and ((next_i, next_j, dir) not in dist or next_score < dist[(next_i, next_j, dir)]):
				dist[(next_i, next_j, dir)] = next_score
				heapq.heappush(nodes, [next_score, next_i, next_j, dir])
		
	
	return dist


def analyze_best_path(end_i, end_j, dist, maze):
	lowest_score = float('inf')
	reverse_start = []
	for dir in range(0, 4):
		reverse_start.append((end_i, end_j, dir))
		lowest_score = min(lowest_score, dist[(end_i, end_j, dir)])


	unique_tiles = set({})
	reverse_dist = get_all_paths(reverse_start, maze)
	for i in range(len(maze)):
		for j in range(len(maze[i])):
			for dir in range(0, 4):
				forward = dist[(i,j,dir)] if (i,j,dir) in dist else None
				backward = reverse_dist[(i,j,(dir + 2) % 4)] if (i,j,(dir + 2) % 4) in dist else None

				if forward is not None and backward is not None and forward + backward == lowest_score:
					unique_tiles.add((i,j))


	return (lowest_score, len(unique_tiles))
	

def main():
	maze = load_input('input.txt')
	start_i, start_j = get_pos('S', maze)
	end_i, end_j = get_pos('E', maze)


	pretty_print(maze)
	print('start', start_i, start_j)
	print('end', end_i, end_j)
	dist = get_all_paths([(start_i, start_j, 1)], maze)
	score, unique_tiles = analyze_best_path(end_i, end_j, dist, maze)
	print('lowest score', score)
	print('lowest score unique tiles', unique_tiles)

if __name__=='__main__':
	main()
