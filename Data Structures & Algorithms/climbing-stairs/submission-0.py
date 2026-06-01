class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1: return 1
        if n == 2: return 2

        two_steps_behind = 1
        one_step_behind = 2

        for i in range(3, n+1):
            current = two_steps_behind + one_step_behind

            two_steps_behind = one_step_behind
            one_step_behind = current
        
        return one_step_behind

        