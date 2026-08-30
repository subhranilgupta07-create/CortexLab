class Solution(object):
    def minimumCost(self, cost):
        cost.sort(reverse = True)
        S = 0
        for i in range (0, len(cost)):
            if ((i + 1) % 3 != 0):
                S += cost[i]
        return S        
