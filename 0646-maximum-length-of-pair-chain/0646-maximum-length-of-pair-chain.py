class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs = sorted(pairs, key = lambda x: x[1])
        answer = []
        for pair in pairs : 
            if len(answer) == 0 :
                answer.append(pair)
            else :
                if pair[0] > answer[-1][1]:
                    answer.append(pair)
        return len(answer)
