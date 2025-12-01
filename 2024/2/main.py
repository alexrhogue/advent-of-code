
def load_input(input_file: str) -> list[list[int]]:
	f = open(input_file, "r")
	lines = f.readlines()

	reports = []

	for line in lines:
		reports.append([int(x) for x in line.split()])

	return reports
      
MAX_STEP_SIZE = 3

def calc_safety(row: list):
	report_dir = 1

	for i in range(len(row) - 1):
		cur = row[i]
		next = row[i+1]
		step_size = next - cur
		step_dir = 1 if step_size > 0 else -1

		if(i == 0):
			report_dir = step_dir

		if(step_size == 0):
			return False
		
		if(step_dir != report_dir):
			return False
		
		if(abs(step_size) > MAX_STEP_SIZE):
			return False
		
	return True

def calc_safety_with_tolerance(row:list):
	sub_reports = []

	for i in range(len(row)):
		start = row[:i]
		end = row[i+1:]
		sub_reports.append(start + end)

	for sub_report in sub_reports:
		if(calc_safety(sub_report)):
			return True
	
	return False


def main():
	reports = load_input("input.txt")
	safe_reports = 0
	safe_reports_with_tolerance = 0
	
	for i in range(len(reports)):
		report = reports[i]
		safe = calc_safety(report)
		
		if(safe):
			safe_reports +=1
			safe_reports_with_tolerance += 1
		else:
			safe_with_tolerance = calc_safety_with_tolerance(report)
			safe_reports_with_tolerance += 1 if safe_with_tolerance else 0
			
	
	print("# safe reports", safe_reports)
	print("# safe reports w/ tolerance", safe_reports_with_tolerance)
    
    
if __name__=="__main__":
	main()
