import re

digit_regex = re.compile(r'\d+')

def load_input(input_file: str):
	f = open(input_file, "r")

	lines = f.readlines()
	antennas = {}
	width = 0
	height = len(lines)
	y = len(lines) - 1
	for line in lines:
		cells = list(line.strip('\n'))
		width = len(cells)

		print(cells)
		for x in range(len(cells)):
			if cells[x] != '.':
				antennas.setdefault(cells[x], []).append((x,y))

		y -= 1

		height = len(lines)

	return (antennas, width, height)

def combinations(num):
	c = []
	i = 0
	while i < num - 1:
		j = i + 1
		while j < num:
			c.append((i, j))
			j += 1
		i += 1

	return c

def calc_antinodes(a, b):
	ax, ay = a
	bx, by = b

	print(ax, ay, bx, by)

	sx = (bx-ax)
	sy = (by-ay)

	print('slope', sx, sy)
	return [(ax - sx, ay - sy), (bx + sx, by + sy)]

def calc_slope(ax, ay, bx, by):
	dx = (bx-ax)
	dy = (by-ay)

	if dx == 0:
		return (0, 1 if dy > 0 else -1)
	
	if dy == 0:
		return ( 1 if dx > 0 else -1, 0)

	gcd = 1
	for val in range(1, 1 + min(abs(dx), abs(dy))):
		if dx / val % 1 == 0 and dy / val % 1 == 0:
			gcd = val
	

	print('slope', dx, dy)
	print('gcd', gcd)
									
	return (int(dx/gcd), int(dy/gcd))


def calc_antinodes_with_resonance(a, b, width, height):
	ax, ay = a
	bx, by = b

	print(ax, ay, bx, by)

	sx, sy = calc_slope(ax, ay, bx, by)
	
	antinodes = [(ax , ay)]

	cx = ax + sx
	cy = ay + sy
	
	while in_bounds(cx, cy, width, height):
		antinodes.append((cx , cy))
		cx += sx
		cy += sy
		

	cx = ax - sx
	cy = ay - sy				
	while in_bounds(cx, cy, width, height):
		antinodes.append((cx , cy))
		cx -= sx
		cy -= sy
		

	print(antinodes)
	return antinodes


def in_bounds(x, y, width, height):
	return x >= 0 and x < width and y >= 0 and y < height

def main():
	antennas, width, height = load_input("input.txt")

	print(antennas, width, height)

	antinodes = set()
	antinodes_with_resonance = set()
	for locs in antennas.values():
		view = [['.' for x in range(width)] for y in range(height)] 
		for line in view:
			print(line)

		options = combinations(len(locs))
		for o in options:
			a = locs[o[0]]
			b = locs[o[1]]
			
			print(a, b)

			for antinode in calc_antinodes(a, b):
				print(antinode)
				if in_bounds(antinode[0], antinode[1], width, height):	
					print('adding', antinode)
					antinodes.add(antinode)
				else:
					print('skipping', antinode)

		
			for antinode in calc_antinodes_with_resonance(a,b,width,height):
				antinodes_with_resonance.add(antinode)
				view[antinode[0]][antinode[1]] = "x"
			
	print(width, height)
	print('unique antinodes', len(antinodes))
	print('unique antinodes w/ resonance', len(antinodes_with_resonance))

    
if __name__=="__main__":
	main()
