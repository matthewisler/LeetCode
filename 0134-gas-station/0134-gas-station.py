class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        current_gas = 0
        start = 0
        #loop thru arrays
        for i in range(0, len(cost)):
            #current gas is equal to how much gas we had plus how much gas we gained and how much gas we spent to get there
            current_gas += (gas[i]-cost[i])
            #if we do not have any gas left
            if current_gas < 0:
                #this didn't work...let's restart and try at the next index
                current_gas = 0
                start = i+1
        
        #if successful then we just return what index we started at
        return start