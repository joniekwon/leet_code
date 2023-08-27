class Solution:
    def canCross(self, stones: List[int]) -> bool:
        n = len(stones)
        jump_dict = {}

        for stone in stones:
            jump_dict[stone] = set()

        jump_dict[0].add(0) 

        for i in range(n):
            for jump_distance in jump_dict[stones[i]]:
                for step in [jump_distance - 1, jump_distance, jump_distance + 1]:
                    if step > 0 and stones[i] + step in jump_dict:
                        jump_dict[stones[i] + step].add(step)
        return len(jump_dict[stones[-1]]) > 0
