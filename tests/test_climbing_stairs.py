from src.climbing_stairs.solution import Solution


class TestClimbingStairs:
    def test_climb_stairs_1(self):
        assert Solution().climbStairs(1) == 1

    def test_climb_stairs_2(self):
        assert Solution().climbStairs(2) == 2

    def test_climb_stairs_3(self):
        assert Solution().climbStairs(3) == 3
