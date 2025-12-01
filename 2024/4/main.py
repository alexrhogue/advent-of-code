from collections import deque

def load_input(input_file: str) -> list[str]:
	f = open(input_file, "r")

	return f.readlines()

def is_in_bounds(dir, map_size) -> bool:
	return  dir[0] >= 0 and dir[0] < map_size and dir[1] >= 0 and dir[1] < map_size

DIRECTIONS = [
		[-1, -1],
		[-1, 0],
		[-1, 1],
		[0, -1],
		[0, 1],
		[1, -1],
		[1, 0],
		[1, 1]
	]


def find_word(map: list[str], target_word: str) -> int: 
	word_count = 0
	first_char = target_word[0]
	queue = deque()

	for i in range(len(map)):
		for j in range(len(map[i])):
			if map[i][j] == first_char:
				for dir in range(len(DIRECTIONS)):
					queue.append([i, j, target_word, dir])

	while len(queue) != 0:
		i, j, substr, dir = queue.popleft()

		if(substr[0] == map[i][j]):
			if len(substr) == 1:
				word_count += 1
			else:
				i2 = i + DIRECTIONS[dir][0]
				j2 = j + DIRECTIONS[dir][1]
				substr2 = substr[1:]

				if is_in_bounds([i2, j2], len(map)):
					queue.append([i2, j2, substr2, dir])

	return word_count

def find_x_mas(map: list[str]) -> int: 
	word_count = 0

	for i in range(1, len(map) - 1):
		for j in range(1, len(map[i]) - 1):
			if map[i][j] == 'A':
				x1 = [map[i-1][j-1], map[i+1][j+1]]
				x2 = [map[i-1][j+1], map[i+1][j-1]]

				x1.sort()
				x2.sort()
			
				if x1 == ['M','S'] and x2 == ['M','S']:
					word_count += 1

	return word_count


def main():
	map = load_input("input.txt")
	word_count = find_word(map, "XMAS")
	x_mas_count = find_x_mas(map)

	print("word count", word_count)
	print("# 'X-MAS'", x_mas_count)
    
if __name__=="__main__":
	main()
