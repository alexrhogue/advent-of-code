
import math
import numpy as np

def load_input(input_file: str) -> list[int]:
	f = open(input_file, 'r')

	return [int(x) for x in list(f.readlines()[0].strip('\n').split(' '))]

def blink(prev:list[int]):
	stones = []

	for s in prev:
		stones += calc_blink(s)

	return stones

def calc_blink(num:int) -> int:
	if num == 0:
		return [1]
	
	num_digits = 1 + math.floor(math.log10(num))

	if num_digits % 2 == 1:
		return [num * 2024]

	t = math.pow(10, num_digits / 2)

	right = math.floor(num % t)
	left = math.floor((num - right)/t)

	return [right, left]


""" def blink_single(start:int, blinks:int) -> int:
	max_size = 1_000_000_000
	size = 1
	arr1 = np.zeros(max_size)
	arr2 = np.zeros(max_size)

	prev = [start]

	for b in range(blinks):
		for i in range(size):
			
		print(len(prev))
		stones = []
		for s in prev:
			if s == 0:
				stones.append(1)
				continue

			num_digits = 1 + math.floor(math.log10(s))

			if num_digits % 2 == 1:
				stones.append(s * 2024)
				continue

			t = math.pow(10, num_digits / 2)

			right = math.floor(s % t)
			left = math.floor((s - right)/t)

			stones.append(left)
			stones.append(right)

		prev = stones.copy()

	return len(prev)
 """

def main():
	stones = load_input('input.txt')
	total_stones = 0
	num_blinks = 25
	
	print('initial arrangement\n', stones)
	for b in range(num_blinks):
		stones = blink(stones)

	total_stones = len(stones)
	print("total stones\n", total_stones)
	assert(total_stones == 207683)

    
if __name__=='__main__':
	main()
