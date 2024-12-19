import re

digit_regex = re.compile(r'\d+')

def load_input(input_file: str) -> list[str]:
	f = open(input_file, "r")

	lines = []
	for line in f.readlines():
		lines.append([int(x) for x in digit_regex.findall(line)])

	return lines

def concat_str(l, r) -> int:
	return int(str(l) + str(r))


def concat_math(l, r) -> int:
	r_size = 10
	while r / r_size >= 1:
		r_size *= 10

	return l * r_size + r

def eval(nums:list[int]) -> list[int]:
	if len(nums) == 0:
		return []
	
	if len(nums) == 1:
		return nums
	
	l = nums[0]
	r = nums [1]
	
	sum = l + r 
	product =  l * r
	joined = concat_math(l, r)

	results = eval([sum] + nums[2:]) + eval([product] + nums[2:]) + eval([joined] + nums[2:])
																					 
	return results

def unconcat_math(l, r) -> int:
	if r >= l:
		return -1
	
	r_size = 10
	while r / r_size >= 1:
		r_size *= 10

	tail = l % r_size

	if tail != r:
		return -1

	return int((l - tail) / r_size)

def is_target_possible(target:int, nums:list[int], debug:bool = False) -> bool:
	targets = [target]

	for i in range(len(nums) - 1, 0, -1):
		if debug: print(targets, nums[i])
		num = nums[i]	

		new_targets = []

		for t in targets:
			dif = t - num
			if debug: print(dif)
			if dif > 0:
				new_targets.append(dif)

			quotient  = t / num
			if debug: print(quotient)
			if quotient == int(quotient):
				new_targets.append(int(quotient))

			trimmed = unconcat_math(t, num)
			if debug: print(trimmed)
			if trimmed != -1:
				new_targets.append(trimmed)

		if debug: print(new_targets)
		targets = new_targets

	return nums[0] in targets


def main():
	lines = load_input("input.txt")
	sum = 0

	for line in lines:
		target = line[0]

		if is_target_possible(target, line[1:]):
			sum += target

	print("sum of successful tests", sum) 

    
if __name__=="__main__":
	main()
