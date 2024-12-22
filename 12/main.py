
def load_input(input_file: str) -> list[int]:
	f = open(input_file, "r")

	garden = []
	for line in f.readlines():
		garden.append(list(line.strip("\n")))

	return garden


def find_plot_price(start_i,start_j, garden, visited:set): 
	area = 0
	perimeter = 0

	plant = garden[start_i][start_j]
	plots = [(start_i,start_j)]
	visited.add((start_i,start_j))

	while len(plots) > 0:
		(i,j) = plots.pop()
		area += 1

		neighbors = [(i-1,j), (i,j+1), (i+1,j), (i, j-1)]

		for n in neighbors:
			i2, j2 = n
			if i2 < 0 or i2 >= len(garden) or j2 < 0 or j2 >= len(garden):
				perimeter += 1

			elif garden[i2][j2] != plant:
				perimeter += 1

			elif n not in visited:
				visited.add(n)
				plots.append(n)

	print('plant', plant)
	print('area', area)
	print('perimeter', perimeter)
	return area * perimeter

def price_all_plots(garden):
	price = 0
	visited = set()
	for i in range(len(garden)):
		for j in range(len(garden[i])):
			if (i,j) not in visited:
				price += find_plot_price(i,j,garden,visited)


	return price



def main():
	garden = load_input("input.txt")
	print(garden)
	assert(len(garden) == len(garden[0]))

	# print(find_plot_price(0, 0, garden, set()))
	print("total cost", price_all_plots(garden))
    
if __name__=="__main__":
	main()
