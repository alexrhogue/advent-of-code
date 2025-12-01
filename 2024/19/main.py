import sys
import heapq
import time

def get_part():
	if len(sys.argv) > 1:
			return 2 if sys.argv[1] == '2' else 1
	
	return 1

def load_input(input_file: str) -> list[str]:
	f = open(input_file, "r")

	lines = f.readlines()
	towels = lines[0].strip().split(', ')
	patterns = []
	for pattern in lines[2:]:
		patterns.append(pattern.strip())

	return (towels, patterns)


def test_design(pattern: str, towels: set[str]):
	tested = set()
	q = []
	heapq.heappush(q, (len(pattern), pattern))
	
	while len(q) > 0:
		_, cur, = heapq.heappop(q)
		
		if cur in tested:
			continue
		
		tested.add(cur)
		if len(cur) == 0:
			return True

		for i in range(0, len(cur)):
			prefix = cur[0:i+1]
			suffix = cur[i+1:]
			if prefix in towels and suffix not in tested:
				heapq.heappush(q, (len(suffix), suffix ))


	return False

def test_patterns(towels, patterns):
	count = 0
	for pattern in patterns:
		if test_design(pattern, towels):
			count += 1

	return count
	
def find_combinations(towels, pattern):
	dp = [0] * (len(pattern) + 1)
	for i in range(1, len(pattern) + 1):
		for j in range(i):
			for towel in towels:
				if j + len(towel) == i and towel == pattern[j:i]:
					if j == 0:
						dp[i] += 1
					else:
						dp[i] += dp[j]

	print(dp)
	return dp[len(pattern)]

	
def main():
	t1 = time.time()
	towels, patterns = load_input('input.txt')

	if get_part() == 1:
		count =  test_patterns(towels, patterns)
		print('# designs possible', count)
	else:
		combinations = 0
		for pattern in patterns:
			combinations += find_combinations(towels, pattern)
			break

		print('# unique combinations', combinations)
		#[print(c) for c in combinations]


	print(f"part {get_part()}: took {round(time.time()-t1, 5)}s")
if __name__=='__main__':
	main()
