
def load_input(input_file: str) -> list[int]:
	f = open(input_file, "r")

	garden = []
	for line in f.readlines():
		garden.append(list(line.strip("\n")))

	return garden


def get_plant(i,j, garden):
	if i < 0 or i >= len(garden) or j < 0 or j >= len(garden):
		return '-'
	
	return garden[i][j]

def count_corners(grid):
	corners = 0
	
	# top left
	if grid[0][0] != grid[1][1] and grid[0][1] == grid[1][1] and grid[1][0] == grid[1][1]:
			corners += 1
	if grid[0][1] != grid[1][1] and grid[1][0] != grid[1][1]:
			corners += 1

	# top right
	if grid[0][2] != grid[1][1] and grid[0][1] == grid[1][1] and grid[1][2] == grid[1][1]:
			corners += 1
	if grid[0][1] != grid[1][1] and grid[1][2] != grid[1][1]:
			corners += 1
	
	# bottom right
	if grid[2][2] != grid[1][1] and grid[2][1] == grid[1][1] and grid[1][2] == grid[1][1]:
			corners += 1
	if grid[2][1] != grid[1][1] and grid[1][2] != grid[1][1]:
			corners += 1
	
	# bottom left
	if grid[2][0] != grid[1][1] and grid[2][1] == grid[1][1] and grid[1][0] == grid[1][1]:
			corners += 1
	if grid[2][1] != grid[1][1] and grid[1][0] != grid[1][1]:
			corners += 1

	return corners

def calc_plot_size(start_i,start_j, garden, visited:set): 
	area = 0
	perimeter = 0
	corners = 0

	plant = garden[start_i][start_j]
	plots = [(start_i,start_j)]
	visited.add((start_i,start_j))

	while len(plots) > 0:
		(i,j) = plots.pop()
		area += 1

		# handle perm 
		for i2,j2 in [(i-1,j), (i,j+1), (i+1,j), (i, j-1)]:
			if(get_plant(i2,j2, garden) != plant):
				perimeter += 1
			elif (i2,j2) not in visited:
				visited.add((i2,j2))
				plots.append((i2,j2))

		
		neighbors = [
			[get_plant(i-1, j-1, garden),get_plant(i-1, j, garden),get_plant(i-1, j+1, garden)],
			[get_plant(i, j-1, garden),get_plant(i, j, garden),get_plant(i, j+1, garden)],
			[get_plant(i+1, j-1, garden),get_plant(i+1, j, garden),get_plant(i+1, j+1, garden)],
		]

		corners += count_corners(neighbors)


	return (area,  perimeter, corners)

def price_all_plots(garden):
	price = 0
	bulk_price = 0
	visited = set()
	for i in range(len(garden)):
		for j in range(len(garden[i])):
			if (i,j) not in visited:
				area, perimeter, corners = calc_plot_size(i,j,garden,visited)
				price += area * perimeter
				bulk_price += area * corners


	return (price, bulk_price)



def main():
	garden = load_input("input.txt")
	assert(len(garden) == len(garden[0]))

	print("total cost", price_all_plots(garden))
    
if __name__=="__main__":
	main()
