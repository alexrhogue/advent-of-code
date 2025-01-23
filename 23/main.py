import sys
import pprint
import time
import functools

def get_part():
	if len(sys.argv) > 1:
			return 2 if sys.argv[1] == '2' else 1
	
	return 1

def load_input(input_file: str) -> list[str]:
	f = open(input_file, "r")

	graph = {}
	for line in f.readlines():
		[a,b] = line.strip().split('-')

		if a not in graph:
			graph[a] = [b]
		else:
			graph[a].append(b)

		if b not in graph:
			graph[b] = [a]
		else:
			graph[b].append(a)


	return graph

def find_network(graph):
	networks = []
	visited = set()
	for a in graph:
		for i in range(len(graph[a])-1):
			b = graph[a][i]

			if b in visited:
				continue

			for j in range(i+1, len(graph[a])):
				c = graph[a][j]

				if c in visited:
					continue

				if b in graph[c] and c in graph[b]:
					if a[0] == 't' or b[0] == 't' or c[0] == 't':
						networks.append([a,b,c])
		
		visited.add(a)



	return networks

def find_largest_network(graph):
	return []

def main():
	t1 = time.time()
	graph = load_input('input.txt')
	pprint.pprint(graph)


	if get_part() == 1:
		networks = find_network(graph)
		pprint.pprint(networks)
		print(f'num networks: {len(networks)}')
	else:
		network = find_largest_network(graph)
		pprint.pprint(network)
		print(f'largest network: {len(network)}')

	print(f"part {get_part()}: took {round(time.time()-t1, 5)}s")
if __name__=='__main__':
	main()
