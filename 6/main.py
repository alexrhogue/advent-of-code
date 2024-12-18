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
	path_size, potential_obstructions = count_map(map)

	print("path size", path_size)
	print("# obstruction options", potential_obstructions)
    
if __name__=="__main__":
	main()
