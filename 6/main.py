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

def in_bounds(pos, map_size):
	if pos[0] < 0 or pos[1] < 0:
		return False

	if pos[0] >= map_size[0] or pos[1] >= map_size[1]:
		return False
	
	return True

def check_for_loop(start_pos, start_dir, map, map_size):
	path = []
	obstacle_pos = get_next_pos(start_pos, start_dir)

	if not in_bounds(obstacle_pos, map_size) or map[obstacle_pos[0]][obstacle_pos[1]] in [START_CHAR, BLOCK_CHAR]:
		return False

	dir = start_dir
	pos = start_pos

	while in_bounds(pos, map_size):  
		if map[pos[0]][pos[1]] == BLOCK_CHAR or (obstacle_pos[0] == pos[0] and obstacle_pos[1] == pos[1]):
			pos = get_prev_pos(pos, dir)
			dir = get_next_dir(dir)
		else:
			path_step = (pos[0], pos[1], dir)
			if path_step in path:
				return True
			path.append(path_step)
			
		pos = get_next_pos(pos, dir)
	
	return False
		
def fill_map(map):
	dir = 0
	pos = find_start_pos(map)
	map_size = (len(map), len(map[0]))

	while in_bounds(pos, map_size):  
		char_at_pos = map[pos[0]][pos[1]]
		if char_at_pos == BLOCK_CHAR:
			pos = get_prev_pos(pos, dir)
			dir = get_next_dir(dir)
		else:
			if char_at_pos == EMPTY_PATH:			
				map[pos[0]][pos[1]] = "X"
			
			if check_for_loop(pos, dir, map, map_size):
				obstruction_pos = get_next_pos(pos, dir)
				map[obstruction_pos[0]][obstruction_pos[1]] = BLOCK_OBSTRUCTION
		
		pos = get_next_pos(pos, dir)

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


def main():
	map = load_input("input.txt")

	fill_map(map)
	
	pretty_print(map)
	
	path_size, potential_obstructions = count_map(map)

	print("path size", path_size)
	print("# obstruction options", potential_obstructions)
    
if __name__=="__main__":
	main()
