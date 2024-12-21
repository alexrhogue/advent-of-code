
def load_input(input_file: str) -> list[int]:
	f = open(input_file, "r")

	top_map = []
	for line in f.readlines():
		top_map.append([int(x) for x in list(line.strip("\n"))])

	return top_map


def get_trail_starts(top_map) -> list[tuple[int, int]]:
	trail_starts = []

	for i in range(len(top_map)):
		for j in range(len(top_map[i])):
			if top_map[i][j] == 0:
				trail_starts.append((i,j))
				
	return trail_starts

def get_neighbors(pos,size) -> list[tuple[int, int]]:
	return list(
		filter(
			lambda p: p[0] >= 0 and p[0] < size and p[1] >= 0 and p[1] < size, 
			[(pos[0]-1, pos[1]), (pos[0], pos[1]-1), (pos[0]+1, pos[1]), (pos[0],pos[1]+1)]
		))

def score_trail(start, top_map) -> int:
	summits = []
	paths = [start]

	while len(paths) > 0:
		cur = paths.pop()
		
		if top_map[cur[0]][cur[1]] == 9:
			summits.append(cur)
			continue

		paths = paths + list(
			filter(
				lambda p: top_map[p[0]][p[1]] == 1 + top_map[cur[0]][cur[1]],
				get_neighbors(cur, len(top_map))
			))

	return (len(set(summits)), len(summits))

def main():
	top_map = load_input("input.txt")
	trail_starts = get_trail_starts(top_map)
	trail_scores = list(map(lambda trail: score_trail(trail, top_map), trail_starts))

	print("topographical map\n", top_map)
	print("trail start positions\n", trail_starts)
	print("trail scores sum\n", sum(list(map(lambda score: score[0], trail_scores))))
	print("trail rating sum\n", sum(list(map(lambda score: score[1], trail_scores))))
    
if __name__=="__main__":
	main()
