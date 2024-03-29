class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        res = 0
        gas_tank = 0
        for i in range(len(gas)):
            gas_tank += (gas[i] - cost[i])
     
            if gas_tank < 0:
                gas_tank = 0
                res = i + 1
                
        return res
            
        