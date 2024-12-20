import re

digit_regex = re.compile(r'\d+')

def load_input(input_file: str) -> list[int]:
	f = open(input_file, "r")

	line = f.readlines()[0]

	return [int(x) for x in list(line.strip("\n"))]


def expand_disk(compacted_disk: list[int]) -> list[int]:
	disk = []
	for i in range(len(compacted_disk)):
		id = '.'
		if i % 2 == 0:
			id = int(i/2)

		for j in range(compacted_disk[i]):
			disk.append(id)

	return disk

def reformat_disk(input_disk: list[int]) -> list[int]:
	disk = input_disk.copy()
	head = 0
	tail = len(disk) - 1

	while head < tail:
		if disk[head] != '.':
			head += 1

		elif disk[tail] == '.':
			tail -= 1

		else:
			swap = disk[tail]
			disk[tail] = disk[head]
			disk[head] = swap

	
	return disk

def reformat_disk_v2(input_disk: list[int]) -> list[int]:
	disk = input_disk.copy()
	head = 0
	head_size = 0
	tail = len(disk) - 1
	tail_size = 0
	tail_key = ''

	while disk[head] != '.':
		head += 1

	head_size = 0
	while disk[head] == '.':
		head_size += 1
		head += 1

	while head_size > 0:
		while disk[tail] == '.':
			tail -= 1

		tail_size = 0
		tail_key = disk[tail]
		while disk[tail] == tail_key:
			tail -= 1
			tail_size += 1

		if tail_size <= head_size:
			for i in range(tail_size):
				h = head - (head_size - i)
				t = tail + (i + 1)
				
				swap = disk[t]
				disk[t] = disk[h]
				disk[h] = swap
			
			head_size -= tail_size


	
	return disk
def calc_checksum(disk: list[int]) -> int:
	check_sum = 0

	for i in range(len(disk)):
		if disk[i] != '.':
			check_sum += (i * disk[i])

	return check_sum
		
def main():
	compacted_disk = load_input("input.txt")
	disk = expand_disk(compacted_disk)
	formatted_disk = reformat_disk(disk)
	checksum = calc_checksum(formatted_disk)
	formatted_disk_v2 = reformat_disk_v2(disk)
	checksum_v2 = calc_checksum(formatted_disk_v2)

	print("compacted\n", compacted_disk)
	print("expanded\n", disk)
	print("formatting v1\n", formatted_disk)
	print("checksum of v1\n", checksum)
	print("formatting v2\n", formatted_disk_v2)
	print("checksum of v2\n", checksum_v2)


    
if __name__=="__main__":
	main()
