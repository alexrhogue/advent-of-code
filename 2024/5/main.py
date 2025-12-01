from collections import deque
import re

digit_regex = re.compile(r'\d+')

class PrintRequest:
	def __init__(self, raw_order_rules, raw_updates):
		self.order_graph = {}
		self.updates = []

		for order_rule in raw_order_rules:
			a, b = digit_regex.findall(order_rule)
			if a in self.order_graph:
				self.order_graph[a].append(b)
			else:
				self.order_graph[a] = [b]


		for update in raw_updates:
			self.updates.append(update.split(','))


	def find_valid_updates(self):
		valid_updates = []

		for update in self.updates:
			if update == self.sort_update(update.copy()):
				valid_updates.append(update)

		return valid_updates
	
	def find_and_sort_invalid_updates(self):
		invalid_updates = []

		for update in self.updates:
			sorted = self.sort_update(update.copy())
			if update != sorted:
				invalid_updates.append(sorted)

		return invalid_updates
	
	def sort_all_updates(self):
		sorted_updates = []

		for update in self.updates:
			sorted_updates.append(self.sort_update(update.copy()))

		return sorted_updates
	
	def sort_update(self, update):
			sorted_update = []

			for i in reversed(range(len(update))):
				j = i - 1

				while j >= 0:
					if update[i] not in self.order_graph:
						break

					if update[j] in self.order_graph[update[i]]:
						swap = update[j]
						update[j] = update[i]
						update[i] = swap
						j = i - 1
					else:
						j -= 1

				sorted_update.insert(0, update[i])

			return sorted_update

	
		
def load_input(input_file: str) -> list[str]:
	f = open(input_file, "r")

	order_rules = []
	updates = []

	is_reading_order_rules = True
	for line in f.readlines():
		sanitized_line = line.strip('\n')
		if sanitized_line == '':
			is_reading_order_rules = False
		elif is_reading_order_rules:
			order_rules.append(sanitized_line)
		else:
			updates.append(sanitized_line)

	return PrintRequest(order_rules, updates)


def get_middle_int(input: list[str]) -> int:
	if len(input) == 0:
		return 0
	
	return int(input[int(len(input)/2)])

def main():
	print_request = load_input("input.txt")
	valid_updates = print_request.find_valid_updates()
	sorted_invalid_updates = print_request.find_and_sort_invalid_updates()

	sum_valid = 0
	for update in valid_updates:
		sum_valid += get_middle_int(update)

		
	sum_invalid = 0
	for update in sorted_invalid_updates:
		sum_invalid += get_middle_int(update)

	print("sum of middle number of correctly ordered updates", sum_valid)
	print("sum of middle number of in-correctly ordered updates", sum_invalid)
    
if __name__=="__main__":
	main()
