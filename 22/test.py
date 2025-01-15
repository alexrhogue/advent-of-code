from main import mix, prune

import unittest

class Test(unittest.TestCase):
    def test_mix(self):
        self.assertEqual(37, mix(42, 15))

    def test_prune(self):
        self.assertEqual(16113920, prune(100000000))

    
if __name__ == '__main__':
    unittest.main()
