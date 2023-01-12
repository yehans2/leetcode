class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        res = 0
        hashmap = {}
        for s in stones:
            if s in hashmap:
                hashmap[s] += 1
            else:
                hashmap[s] = 1
        for jewel in jewels:
            if jewel in hashmap:
                res += hashmap[jewel]
        return res
                
            
        