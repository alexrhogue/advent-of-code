from main import PrintRequest, get_middle_int

import unittest

class Test(unittest.TestCase): 
	simple_order_input = ["1|2", "2|3"]
	simple_updates_input = ["1,2,3", "2,3", "3,1", "2,1,3"]


	def test_print_request_init(self): 
		pr = PrintRequest(self.simple_order_input, self.simple_updates_input)
		self.assertEqual({"1": ["2"], "2": ["3"]}, pr.order_graph)
		self.assertEqual([["1", "2", "3"], ["2", "3"], ["3", "1"], ["2", "1", "3"]], pr.updates)


	def test_sort_all_updates_simple(self): 
		pr = PrintRequest(self.simple_order_input, self.simple_updates_input)

		self.assertEqual([["1", "2", "3"], ["2", "3"], ["3", "1"], ["1", "2", "3"]], pr.sort_all_updates())

	def test_sort_all_update_complex(self):
		pr = PrintRequest(["47|53", "97|13", "97|61", "97|47", "75|29", "61|13", "75|53", "29|13", "97|29", "53|29", "61|53", "97|53", "61|29", "47|13", "75|47", "97|75", "47|61", "75|61", "47|29", "75|13", "53|13"],
											["75,47,61,53,29", "97,61,53,29,13", "75,29,13", "75,97,47,61,53", "61,13,29", "97,13,75,29,47"])
		
		self.assertEqual([["75","47","61","53","29"], ["97","61","53","29","13"], ["75","29","13"], ["97","75","47","61","53"], ["61","29","13"], ["97", "75", "47", "29", "13"]], pr.sort_all_updates())


	def test_get_middle_int(self):
		self.assertEqual(0, get_middle_int([]))
		self.assertEqual(2, get_middle_int(["1", "2", "3"]))
		self.assertEqual(2, get_middle_int(["1", "2"]))
		self.assertEqual(3, get_middle_int(["1", "2", "3", "4"]))
		self.assertEqual(3, get_middle_int(["1", "2", "3", "4", "5"]))
			
if __name__ == '__main__':
    unittest.main()
