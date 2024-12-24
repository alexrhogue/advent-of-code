
import math
from collections import Counter


def load_input(input_file: str) -> list[int]:
	f = open(input_file, 'r')

	return [int(x) for x in list(f.readlines()[0].strip('\n').split(' '))]


def blink(stones:Counter) -> int:
	result = Counter()
	for stone, count in stones.items():
		if stone == 0:
			result[1] += count
		else:
			num_digits = 1 + math.floor(math.log10(stone))

			if num_digits % 2 == 1:
				result[stone * 2024] += count
			else:
				t = math.pow(10, num_digits / 2)
				right = math.floor(stone % t)
				left = math.floor((stone - right)/t)

				result[right] += count
				result[left] += count

	return result

def main():
	stones = Counter(load_input('input.txt'))
	num_blinks = 75

	for i in range(num_blinks):
		stones = blink(stones)
		
	total_stones = sum(stones.values())
	print("total stones\n", total_stones)

    
if __name__=='__main__':
	main()
