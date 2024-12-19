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



def main():
	lines = load_input("input.txt")
	sum = 0

	for line in lines:
		target = line[0]
		results = eval(line[1:])

		if target in results:
			sum += target

	print("sum of successful tests", sum) 

    
if __name__=="__main__":
	main()
