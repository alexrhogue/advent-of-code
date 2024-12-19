import multiprocessing

def load_input(input_file: str) -> list[str]:
	f = open(input_file, "r")

	map = []
	for line in f.readlines():
		map.append(list(line.strip('\n')))

	return map

START_CHAR = '^'
BLOCK_CHAR = "#"
PATH_CHAR = "X"
BLOCK_OBSTRUCTION = "O"
EMPTY_PATH = '.'

DIRECTIONS = [
	(-1,0),	
	(0,1),
	(1,0),
	(0,-1)
]

def find_start_pos(map):
	for i in range(len(map)):
		for j in range(len(map[i])):
			if map[i][j] == START_CHAR:
				return (i, j)

def get_next_pos(pos, dir):
	return (pos[0] + DIRECTIONS[dir][0], pos[1] + DIRECTIONS[dir][1])

def get_prev_pos(pos, dir):
	return get_next_pos(pos, get_reverse_dir(dir))

def get_next_dir(dir):
	return (dir + 1) % len(DIRECTIONS)

def get_reverse_dir(dir):
	return (dir + 2) % len(DIRECTIONS)

def get_char(pos, map):
	return map[pos[0]][pos[1]]

def set_char(val, pos, map):
	map[pos[0]][pos[1]] = val

def in_bounds(pos, map_size):
	if pos[0] < 0 or pos[1] < 0:
		return False

	if pos[0] >= map_size[0] or pos[1] >= map_size[1]:
		return False
	
	return True

def is_next_pos_blocked(pos, dir, map, map_size):
	next_pos = get_next_pos(pos, dir)

	if not in_bounds(next_pos, map_size):
		return False
	
	if get_char(next_pos, map) == BLOCK_CHAR:
		return True
	
	return False
	

def get_next_move(pos, dir, map, map_size):
		next_dir = dir

		# rotate until next position is clear
		while is_next_pos_blocked(pos, next_dir, map, map_size):
			next_dir = get_next_dir(next_dir)

		next_pos = get_next_pos(pos, next_dir)

		return ( next_pos, next_dir )

def has_loop(start_pos, start_dir, map, map_size):
	path = []
	pos = start_pos
	dir = start_dir

	while in_bounds(pos, map_size):
		path_step = (pos[0], pos[1], dir)
		if path_step in path:
			return True
		
		path.append(path_step)

		pos, dir = get_next_move(pos, dir, map, map_size)

	return False

def fill_map(map):
	pos = find_start_pos(map)
	dir = 0
	map_size = (len(map), len(map[0]))

	while in_bounds(pos, map_size):
		# mark current cell
		if get_char(pos, map) == EMPTY_PATH:			
			set_char(PATH_CHAR, pos, map)
		
		# find next legal move
		next_pos, next_dir = get_next_move(pos, dir, map, map_size)

		if in_bounds(next_pos, map_size):
			next_char = get_char(next_pos, map)

			if next_char is EMPTY_PATH:
				set_char(BLOCK_CHAR, next_pos, map)

				if has_loop(pos, next_dir, map, map_size):
					set_char(BLOCK_OBSTRUCTION, next_pos, map)
				else:
					set_char(next_char, next_pos, map)

		pos = next_pos
		dir = next_dir


def get_path(pos, dir, map):
	path = []
	has_loop = False
	map_size = (len(map), len(map[0]))

	while in_bounds(pos, map_size):
		if (pos,dir) in path:
			has_loop = True
			break

		path.append((pos, dir))
		pos, dir = get_next_move(pos, dir, map, map_size)

	return (path, has_loop)

def count_map(map):
	path_size = 0; 
	potential_obstructions = 0

	for i in range(len(map)):
		for j in range(len(map[i])):
			if map[i][j] in [START_CHAR, PATH_CHAR]:
				path_size += 1
			if map[i][j] == BLOCK_OBSTRUCTION:
				path_size += 1
				potential_obstructions += 1
	
	return (path_size, potential_obstructions)


def pretty_print(map):
	for line in map:
		print(line)

def worker(id, input, map, return_dict):
		(pos, dir, obstacle_pos) = input

		map[obstacle_pos[0]][obstacle_pos[1]] = BLOCK_CHAR

		(path, has_loop) = get_path(pos, dir, map)

		return_dict[id] = has_loop

def main():
	input_map = load_input("input.txt")

	start_pos = find_start_pos(input_map)
	start_dir = 0
	(path, has_loop) = get_path(start_pos, start_dir, input_map)

	print("path found")

	visited = set()
	potential_obstacles = []
	for i in range(len(path) -1):
		pos, dir = path[i]
		if pos in visited:
			continue

		visited.add(pos)

		next_pos = path[i+1][0]
		if next_pos in visited:
			continue

		potential_obstacles.append((pos, dir, next_pos))



	manager = multiprocessing.Manager()
	total_items = len(potential_obstacles)
	jobs = []
	batch_count = 0
	batch_size = 24
	return_dict = manager.dict()

	while batch_size * batch_count < total_items:
		print(f"\rprocessing batch # {batch_count + 1}/{int(total_items/batch_size)}", end="")

		start = batch_count * batch_size
		end = min((batch_count + 1) * batch_size, total_items)
			
		for j in range(start, end):
			p = multiprocessing.Process(target=worker, args=(j, potential_obstacles[j], input_map, return_dict))
			jobs.append(p)
			p.start()

		for p in jobs:
			p.join()

		batch_count += 1
		
		
	
	print("\n----")
	path_size = len(set(map(lambda c: c[0], path)))
	print("path size", path_size)

	num_options = len(list(filter(bool, return_dict.values())))
	print("obstruction options count", num_options)
    
if __name__=="__main__":
	main()
