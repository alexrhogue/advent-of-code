def min_cost_to_climb_stairs(cost):
    """
    Calculate the minimum cost to climb to the top of a staircase where you can either take one or two steps.

    :param cost: List[int], a list where cost[i] is the cost of stepping on the ith step.
    :return: int, the minimum cost to reach the top.
    """

    dp = cost + [0]
    for i in range(2, len(cost) + 1):
        dp[i] = dp[i] + min(dp[i-1], dp[i-2])


    return dp[-1]

if __name__ == "__main__":
    import unittest

    class TestMinCostToClimbStairs(unittest.TestCase):

        def test_example_cases(self):
            self.assertEqual(min_cost_to_climb_stairs([10, 15, 20]), 15)
            self.assertEqual(min_cost_to_climb_stairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]), 6)

        def test_empty_stairs(self):
            self.assertEqual(min_cost_to_climb_stairs([]), 0)

        def test_single_step(self):
            self.assertEqual(min_cost_to_climb_stairs([10]), 0)

        def test_two_steps(self):
            self.assertEqual(min_cost_to_climb_stairs([10, 15]), 10)

        def test_large_stairs(self):
            self.assertEqual(min_cost_to_climb_stairs([1] * 1000), 500)
            self.assertEqual(min_cost_to_climb_stairs([100, 1, 100, 1, 1, 100, 1, 1, 1, 100]), 5)

    unittest.main()
