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

	start = []
	for num in f.readlines():
		start.append(int(num.strip()))

	return start

def mix(a,b):
	return a^b 

def prune(a):
	return a % 16777216

def step(num):
		result = prune(mix(num, num * 64))
		result = prune(mix(result, int(result / 32)))
		result = prune(mix(result, result * 2048))
		
		return result

def calc(nums, sims):
	sum = 0
	for num in nums:
		result = num
		for i in range(sims):
			result = step(result)

		print(f"{num}: {result}")
		sum += result


	return sum

def calc_seq(nums, sims):
	f = {}

	for i in range(len(nums)):
		result = nums[i]
		seq = []
		for j in range(sims):
			next = step(result)
			next_price = next % 10

			seq.append(next_price - (result % 10))

			if j > 2:
				s = tuple(seq[j-3: j+1])
				if i == 0:
					if s in f:
						f[s][i] = max(f[s][i], next_price)
					else:
						f[s] = [next_price]

				elif s in f:
					if len(f[s]) > i:
						f[s][i] = max(f[s][i], next_price)
					else:
						f[s].append(next_price)

			result = next

	highest_price = 0
	for key in f:
		highest_price = max(highest_price, sum(f[key]))

	return highest_price

def main():
	t1 = time.time()
	input = load_input('input.txt')

	sims = 2000
	sum = 0

	if get_part() == 1:
		sum = calc(input, sims)
		print(f'sum of input after {sims} simulations: {sum}')
	else:
		banana = calc_seq(input, sims)
		print(f'num bananas after {sims} simulations: {banana}')

	print(f"part {get_part()}: took {round(time.time()-t1, 5)}s")
if __name__=='__main__':
	main()
