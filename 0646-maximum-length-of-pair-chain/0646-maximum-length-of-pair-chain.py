class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        sortedPairs = sorted(pairs, key = lambda x: x[1]);output = []
        for pair in sortedPairs : 
            if len(output) == 0 :output.append(pair)
            else :
                if pair[0] > output[-1][1] :output.append(pair)
        return len(output)
