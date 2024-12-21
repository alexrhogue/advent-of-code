
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

def blink_dfs(num:int, i:int, depth: int) -> int:
	if i == depth:
		return 1
	
	if num == 0:
		return blink_dfs(1, i+1, depth)
	
	num_digits = 1 + math.floor(math.log10(num))

	if num_digits % 2 == 1:
		return blink_dfs(num*2024, i+1, depth)

	t = math.pow(10, num_digits / 2)

	right = math.floor(num % t)
	left = math.floor((num - right)/t)

	return blink_dfs(left, i+1, depth) + blink_dfs(right, i+1, depth)
	

def main():
	stones = load_input('input.txt')
	total_stones = 0
	num_blinks = 75
	total_stones = 0

	for s in stones:
		print("processing stone", s)
		total_stones += blink_dfs(s, 0, num_blinks)

	print("total stones\n", total_stones)
	assert(total_stones == 207683)

    
if __name__=='__main__':
	main()
